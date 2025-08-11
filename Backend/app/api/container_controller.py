from fastapi import APIRouter, Query
from typing import Optional
from app.models.container import ContainerIn, ContainerOut
from app.services import docker_service

router = APIRouter()

#GET
@router.get("/contenedores", response_model=list[ContainerOut])
async def Lista_contenedores(id: Optional[int] = Query(None),
                            name: Optional[str] = Query(None),
                            status: Optional[str] = Query(None),
                            image: Optional[str] = Query(None)):
    return await docker_service.lista_contenedores(id=id, name=name, status=status, image=image)

@router.get("/contenedores/{id}", response_model=ContainerOut)
async def Obtener_contenedor(id: int):
    return await docker_service.obtener_contenedor(id)

#POST
@router.post("/contenedores", response_model=ContainerOut)
async def Crear_contenedor(data: ContainerIn):
    return await docker_service.crear_contenedor(data)

#PUT
@router.put("/contenedores/{id}", response_model=ContainerOut)
async def Actualizar_contendor(id: int, data: ContainerIn):
    return await docker_service.actualizar_contendor(id, data)

#DELETE
@router.delete("/contenedores/{id}")
async def Borrar_contenedor(id: int):
    return await docker_service.borrar_contenedor(id)
