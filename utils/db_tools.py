import psycopg2
from settings.db_auth import *
import logging


class DbManager:
    def __init__(self):
        pass

    def _connect(self):
        try:
            self._conn = psycopg2.connect(user=USERNAME,
                                          password=PASSWORD,
                                          host=HOST,
                                          dbname=DB_NAME)

            self._cur = self._conn.cursor()

        except Exception as err:
            logging.error("DB CONNECTION FAILED")

    def _close(self):
        self._cur.close()
        self._conn.close()

    def _execute(self, query_str):
        self._cur.execute(query_str)
        return self._cur.fetchall()

    def execute_select(self, query_str):
        self._connect()
        data = self._execute(query_str)
        self._close()

        return data


if __name__ == '__main__':
    o = DbManager()
