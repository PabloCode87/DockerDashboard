from fastapi import APIRouter
from app.db.client import prisma
from app.models.container import ContainerOut

router = APIRouter()

@router.get("/contenedores", response_model=list[ContainerOut])
async def lista_contenedores():
    contenedores=await prisma.dockercontainer.find_many()
    return contenedores