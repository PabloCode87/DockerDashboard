from fastapi import APIRouter, Query
from app.models.logEntry import LogEntryCreate, LogEntry
from app.services import log_service

router = APIRouter()

#GET
@router.get("/logs/{containerId}")
async def Lista_logs(containerId:str):
    logs= await log_service.obtenerLogsContenedor(containerId)
    return {"count":len(logs), "logs":logs}

#POST
@router.post("/logs", response_model=LogEntry)
async def Crear_logs(logData: LogEntryCreate):
    return await log_service.crearLogEntry(logData)