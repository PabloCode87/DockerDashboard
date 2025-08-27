-- CreateTable
CREATE TABLE "public"."ContainerMetrics" (
    "id" SERIAL NOT NULL,
    "containerId" TEXT NOT NULL,
    "cpuUsage" DOUBLE PRECISION NOT NULL,
    "memoryUsage" DOUBLE PRECISION NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "ContainerMetrics_pkey" PRIMARY KEY ("id")
);
