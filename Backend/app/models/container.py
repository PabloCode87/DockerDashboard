import datetime
from pydantic import BaseModel
from typing import Optional

class ContainerOut(BaseModel):
    id:str
    name:str
    status:str
    image:str
    cpuUsage:Optional[float] = None
    memoryUsage:Optional[float]=None
    
    class Config:
        orm_mode=True
        
class ContainerCreate(BaseModel):
    name:str
    image:str
    
