from app.models.logEntry import LogEntryCreate, LogEntry
from app.services.exception_handler import manejar_errores_servicio
from app.db.client import prisma
from typing import List, Optional

@manejar_errores_servicio
async def crearLogEntry (logData: LogEntryCreate) -> LogEntry:
    return await prisma.logentry.create(
        data={
            "containerId": logData.containerId,
            "message": logData.message,
            "level": logData.level,
            "timestamp":logData.timestamp
        }
    )

@manejar_errores_servicio
async def obtenerLogsContenedor(containerId: str):
    return await prisma.logentry.find_many(
        where={"containerId":containerId},
        order={"timestamp":"desc"}
    )