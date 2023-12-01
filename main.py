from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.event import Event
from services.events.create_event import CreateEvent
from services.events.list_event import ListEvent

app = FastAPI()

events = []

@app.get("/")
def read_root():
    return {"code": 200, "message": "ok"}

@app.get("/events")
def list_events():
    # events = ListEvent()
    return {"code": 200, "events": events}

@app.post("/events")
def create_event(event_data: Event):
    try:
        print(event_data.to_dict())
        create_event_service = CreateEvent(event_data)
        create_event_service.execute()
        events.append(create_event_service.event.dict())
        return {"code": 200, "event": create_event_service.event.dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
