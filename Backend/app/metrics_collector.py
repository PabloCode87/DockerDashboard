import asyncio
from datetime import datetime, timedelta
from app.db.client import prisma

COLLECTION_INTERVAL = 30
CLEAN_INTERVAL = 24 * 60 * 60

async def collect_metrics():
    containers = await prisma.dockercontainer.find_many()

    for container in containers:
        cpu = container.cpuUsage or 0
        memory = container.memoryUsage or 0

        await prisma.containermetrics.create(
            data={
                "containerId": container.containerId,
                "cpuUsage": cpu,
                "memoryUsage": memory,
                "collectedAt": datetime.utcnow(),
            }
        )

async def populate_historical_metrics():
    containers = await prisma.dockercontainer.find_many()

    for container in containers:
        await prisma.containermetrics.create(
            data={
                "containerId": container.containerId,
                "cpuUsage": container.cpuUsage or 0,
                "memoryUsage": container.memoryUsage or 0,
                "collectedAt": container.createdAt,
            }
        )

    logs = await prisma.logentry.find_many()
    for log in logs:
        await prisma.containermetrics.create(
            data={
                "containerId": log.containerId,
                "cpuUsage": 0,
                "memoryUsage": 0,
                "collectedAt": log.timestamp,
            }
        )


async def schedule_metrics_collection():
    try:
        await populate_historical_metrics()
    except Exception as e:
        print(f"Error poblando métricas históricas: {e}")

    while True:
        try:
            await collect_metrics()
        except Exception as e:
            print(f"Error recolectando métricas: {e}")
        await asyncio.sleep(COLLECTION_INTERVAL)

async def clean_old_metrics():
    while True:
        try:
            cutoff = datetime.utcnow() - timedelta(days=60)  # últimos 2 meses
            deleted = await prisma.containermetrics.delete_many(
                where={"collectedAt": {"lt": cutoff}}
            )
            print(f"[Metrics Cleaner] Eliminados {deleted} registros antiguos")
        except Exception as e:
            print(f"[Metrics Cleaner] Error limpiando métricas: {e}")
        await asyncio.sleep(CLEAN_INTERVAL)