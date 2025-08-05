from fastapi import FastAPI
from prisma import Prisma

app=FastAPI()
prisma=Prisma()

@app.on_event("startup")
async def startup():
    await prisma.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
    
@app.get("/")
async def root():
    return{"messeage": "Docker Dashboard Backend OK"}


@app.get("/containers")
async def list_containers():
    containers = await prisma.dockercontainer.find_many()
    return containers