import datetime
from models.event import Event
from repositories.event_repository import EventRepository

class BaseEvent:
    def __init__(self, event_data=None):
        self.event_repository = EventRepository()
        #if event_data:
        #    self.event = Event(
        #        customer_id=event_data["customer_id"],
        #        event_type=event_data["event_type"],
        #        timestamp=datetime.datetime.strptime(event_data["timestamp"], "%Y-%m-%dT%H:%M:%S"),
        #        email_id=event_data["email_id"],
        #        clicked_link=event_data["clicked_link"]
        #    )
        self.event = event_data

    def execute(self):
        pass
