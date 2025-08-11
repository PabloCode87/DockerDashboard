from pydantic import BaseModel
from typing import Optional

class ContainerOut(BaseModel):
    id:int
    name:str
    status:str
    image:str
    cpuUsage:Optional[float] = None
    memoryUsage:Optional[float]=None
    
    class Config:
        orm_mode=True
        
class ContainerIn(BaseModel):
    containerId:str
    name: str
    status: str
    image: str
    cpuUsage: Optional[float] = None
    memoryUsage: Optional[float] = None
