from fastapi import APIRouter, Query
from app.models.alert import AlertCreate, Alert
from app.services import alert_service
from typing import List

router = APIRouter()

#Gets
@router.get("/alerts", response_model=List[Alert])
async def listar_alertas(containerId: str | None = Query(None)):
    return await alert_service.obtener_alertas(containerId)


#Posts
@router.post("/alerts", response_model=Alert)
async def crear_alerta(alertData: AlertCreate):
    return await alert_service.crear_alerta(alertData)