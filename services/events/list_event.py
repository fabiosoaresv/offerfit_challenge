from services.events.base_event import BaseEvent

class ListEvent(BaseEvent):
    def __init__(self, event_data = None):
        super().__init__(event_data)

    def execute(self):
        return self.event_repository.list()