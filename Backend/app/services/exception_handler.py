import logging
from fastapi import HTTPException

logger = logging.getLogger("app.services")

def manejar_errores_servicio(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error en servicio {func.__name__}: {e}", exc_info=True)
            raise HTTPException(
                status_code=500,
                detail="Ocurrió un error interno en el servidor."
            )
    return wrapper