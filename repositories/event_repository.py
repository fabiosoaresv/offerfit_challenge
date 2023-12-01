from repositories.database import PostgresConnection

class EventRepository:
    def __init__(self):
        self.pg_connection = PostgresConnection()
        self.pg_connection.connect()

    def create(self, event):
        query = """
        INSERT INTO events (customer_id, event_type, timestamp, email_id, clicked_link)
        VALUES (
            %(event.customer_id)s,
            %(event.event_type)s,
            %(event.timestamp)s,
            %(event.email_id)s,
            %(event.clicked_link)s)
        RETURNING *;
        """
        return self.pg_connection.execute_query(query)

    def list(self):
        query = "SELECT * FROM events;"
        return self.pg_connection.execute_query(query)
