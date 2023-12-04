import datetime
from repositories.database import PostgresConnection

class EventRepository:
    def __init__(self):
        self.pg_connection = PostgresConnection()
        self.pg_connection.connect()

    def create(self, event):
        query = f"""
        INSERT INTO events (customer_id, event_type, timestamp, email_id, clicked_link)
        VALUES ({event.customer_id}, '{event.event_type}', '{event.timestamp}', {event.email_id}, '{event.clicked_link}')
        RETURNING *;
        """

        self.pg_connection.execute_query(query)
        self.pg_connection.close_connection()

    def list(self):
        query = "SELECT * FROM events;"
        result = self.pg_connection.execute_query(query)
        self.pg_connection.close_connection()
        return self._format_result(result[1])

    def _format_result(self, result):
        print('meu resultado')
        print(result)
        columns = [desc[0] for desc in self.pg_connection.cursor.description]
        return [{columns[i]: row[i] for i in range(len(columns))} for row in result]
