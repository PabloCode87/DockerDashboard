from app.models.alert import AlertCreate, Alert
from app.services.exception_handler import manejar_errores_servicio
from app.db.client import prisma

@manejar_errores_servicio
async def crear_alerta(alertData: AlertCreate) -> Alert:
    return await prisma.alert.create(
        data={
            "containerId": alertData.containerId,
            "name": alertData.name,
            "condition": alertData.condition,
            "threshold": alertData.threshold,
        }
    )


@manejar_errores_servicio
async def obtener_alertas(containerId: str | None = None):
    filtros = {"containerId": containerId} if containerId else {}
    return await prisma.alert.find_many(
        where=filtros,
        order={"createdAt": "desc"}
    )