from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Event(BaseModel):
    customer_id: int
    event_type: str
    timestamp: datetime
    email_id: int
    clicked_link: Optional[str] = None

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "event_type": self.event_type,
            "timestamp": self.timestamp.isoformat(),
            "email_id": self.email_id,
            "clicked_link": self.clicked_link,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
