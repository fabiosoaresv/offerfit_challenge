#from pydantic import BaseModel
from datetime import datetime
from typing import Optional
#
#class Event(BaseModel):
#    customer_id: int
#    event_type: str
#    timestamp: datetime
#    email_id: int
#    clicked_link: Optional[str] = None
#
#    def to_dict(self):
#        return {
#            "customer_id": self.customer_id,
#            "event_type": self.event_type,
#            "timestamp": self.timestamp.isoformat(),
#            "email_id": self.email_id,
#            "clicked_link": self.clicked_link,
#        }
#
#    @classmethod
#    def from_dict(cls, data):
#        return cls(**data)
from sqlmodel import SQLModel, Field


class EventBase(SQLModel):
    customer_id: int
    event_type: str
    timestamp: str
    email_id: int
    clicked_link: Optional[str] = None


class Event(EventBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class EventCreate(EventBase):
    pass