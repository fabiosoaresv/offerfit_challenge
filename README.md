## Build mannually
```sh
$ pip3 install -r requirements.txt
$ uvicorn main:app --reload
```

## Execute request
1. Create a new event
```sh
$ curl -X POST http://127.0.0.1:8000/events -H "Content-Type: application/json" -d '{"customer_id": 123, "event_type": "email_click", "timestamp": "2023-10-23T14:30:00", "email_id": 1234, "clicked_link": "https://example.com/some-link"}'
```

*Response:*
```sh
{"code":200,"event":{"customer_id":456,"event_type":"email_open","timestamp":"2023-10-24T11:30:00","email_id":998,"clicked_link":null}}%
```

2. List all events
```sh
$ curl -X GET http://127.0.0.1:8000/events -H "Content-Type: application/json"
```

*Response:*
```sh
{"code":200,"events":[{"customer_id":456,"event_type":"email_open","timestamp":"2023-10-24T11:30:00","email_id":998,"clicked_link":null},{"customer_id":123,"event_type":"email_click","timestamp":"2023-10-23T14:30:00","email_id":1234,"clicked_link":"https://example.com/some-link"}]}%
```

## Next steps
1. Finish to implement the connection with Postgres + migration
2. Write unit and integration tests
3. Finish to dockerize the project
4. Improve the documentation
5. Deploy in Digital Ocean


## Annotations (running migrations)
```sh
createdb offerfit_development -h localhost -U postgres
alembic revision --autogenerate -m "create_event_table"
alembic upgrade head --verbose
```