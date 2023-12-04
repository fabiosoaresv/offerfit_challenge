from services.events.base_event import BaseEvent


class CreateEvent(BaseEvent):
    def __init__(self, event_data):
        super().__init__(event_data)

    def execute(self):
        self.event_repository.create(self.event)
        self.event