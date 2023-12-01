from services.events.base_event import BaseEvent

class ListEvent():
    def __init__(self, event_data = None):
        super().__init__(event_data)

    def execute(self):
        self.event_repository.list()