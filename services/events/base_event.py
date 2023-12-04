import datetime
from models.event import Event
from repositories.event_repository import EventRepository

class BaseEvent:
    def __init__(self, event_data=None):
        self.event_repository = EventRepository()
        self.event = event_data

    def execute(self):
        pass
