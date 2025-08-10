from fastapi import APIRouter
from app.models.container import ContainerIn, ContainerOut
from app.services import docker_service

router = APIRouter()

#GET
@router.get("/contenedores", response_model=list[ContainerOut])
async def lista_contenedores():
    return await docker_service.lista_contenedores()

@router.get("/contenedores/{id}", response_model=ContainerOut)
async def obtener_contenedor(id: int):
    return await docker_service.obtener_contenedor(id)

#POST
@router.post("/contenedores", response_model=ContainerOut)
async def crear_contenedor(data: ContainerIn):
    return await docker_service.crear_contenedor(data)

#PUT
@router.put("/contenedores/{id}", response_model=ContainerOut)
async def actualizar_contendor(id: int, data: ContainerIn):
    return await docker_service.actualizar_contendor(id, data)

#DELETE
@router.delete("/contenedores/{id}")
async def borrar_contenedor(id: int):
    return await docker_service.borrar_contenedor(id)
