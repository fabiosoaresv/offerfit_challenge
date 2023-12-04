import os
import psycopg2

class PostgresConnection:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'offerfit_development'
        self.user = 'postgres'
        self.password = 'postgres'
        self.port = '5432'
        self.literal_binds = True
        self.connection = None
        self.cursor = None

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.connection.commit()
            print("Query executed successfully.")
            return True, result

        except psycopg2.Error as e:
            print("Error to execute query:", e)
            return False, e

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected.")

        except psycopg2.Error as e:
            print("Error to connect in PostgreSQL:", e)

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed.")
