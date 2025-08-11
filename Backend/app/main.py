from fastapi import FastAPI
from app.db.client import prisma
from app.api.container_controller import router as contenedores_router
from app.api.log_controller import router as log_controller

app=FastAPI()

@app.on_event("startup")
async def startup():
    await prisma.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
    
@app.get("/")
async def root():
    return{"messeage": "Docker Dashboard Backend OK"}


app.include_router(contenedores_router)
app.include_router(log_controller)