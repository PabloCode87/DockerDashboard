import random
from typing import Optional
from fastapi import HTTPException
from app.db.client import prisma
from app.models.container import ContainerIn, ContainerOut
from app.services.exception_handler import manejar_errores_servicio

#GET
@manejar_errores_servicio
async def lista_contenedores(id: Optional[int] = None,name: Optional[str] = None,
                            status: Optional[str] = None,
                            image: Optional[str] = None,) -> list[ContainerOut]:
    filtros = {}
    if id is not None:
        filtros['id'] = id
    if name:
        filtros['name'] = {'contains': name, 'mode': 'insensitive'}
    if status:
        filtros['status'] = {'equals': status, 'mode': 'insensitive'}
    if image:
        filtros['image'] = {'contains': image, 'mode': 'insensitive'}

    return await prisma.dockercontainer.find_many(where=filtros)

@manejar_errores_servicio
async def obtener_contenedor(id: int) -> ContainerOut:
    contenedor = await prisma.dockercontainer.find_unique(where={"id": id})
    if not contenedor:
        raise HTTPException(status_code=404, detail="Contenedor no encontrado")
    return contenedor

#POST
@manejar_errores_servicio
async def crear_contenedor(data: ContainerIn) -> ContainerOut:
    cpu = data.cpuUsage if data.cpuUsage is not None else round(random.uniform(0, 12), 1)
    mem = data.memoryUsage if data.memoryUsage is not None else round(random.uniform(0, 250), 1)
    return await prisma.dockercontainer.create(
        data={
            "containerId":data.containerId,
            "name": data.name,
            "status": data.status,
            "image":data.image,
            "cpuUsage": cpu,
            "memoryUsage": mem,
            })

#PUT
@manejar_errores_servicio
async def actualizar_contendor(id: int, data: ContainerIn) -> ContainerOut:
    cpu = data.cpuUsage if data.cpuUsage is not None else round(random.uniform(0, 12), 1)
    mem = data.memoryUsage if data.memoryUsage is not None else round(random.uniform(0, 250), 1)
    contenedor = await prisma.dockercontainer.update(
        where={"id": id},
        data={
            "containerId":data.containerId,
            "name": data.name,
            "status": data.status,
            "image":data.image,
            "cpuUsage": cpu,
            "memoryUsage": mem,
            }
    )
    if not contenedor:
        raise HTTPException(status_code=404, detail="Contenedor no encontrado")
    return contenedor

#DELETE
@manejar_errores_servicio
async def borrar_contenedor(id: int):
    await prisma.dockercontainer.delete(where={"id": id})
    return {"message": "Contenedor eliminado"}

