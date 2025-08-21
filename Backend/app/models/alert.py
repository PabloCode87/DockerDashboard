from pydantic import BaseModel
from datetime import datetime

class AlertBase(BaseModel):
    containerId: str
    name: str
    condition: str
    threshold: float
    
class AlertCreate(BaseModel):
    containerId: str
    name: str
    condition: str
    threshold: float

class Alert(BaseModel):
    id:int
    createdAt: datetime
    
    class Config:
        orm_mode=True