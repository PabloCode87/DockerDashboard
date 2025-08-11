from pydantic import BaseModel
from datetime import datetime

class LogEntryBase(BaseModel):
    containerId:str
    message:str
    level:str
    timestamp: datetime | None = None
    
class LogEntryCreate(BaseModel):
    containerId:str
    message:str
    level:str
    timestamp: datetime | None = None

class LogEntry(BaseModel):
    id:int
    
    class Config:
        orm_mode=True