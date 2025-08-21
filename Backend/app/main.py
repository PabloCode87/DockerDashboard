from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.client import prisma
from app.api.container_controller import router as contenedores_router
from app.api.log_controller import router as log_controller
from app.api.alert_controller import router as alert_controller

app=FastAPI()

#Configuramos CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
app.include_router(alert_controller)