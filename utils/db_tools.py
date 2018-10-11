import psycopg2
from settings.db_auth import *
import logging


class DbManager:
    """
    @description: context manager protocol based utility class
    """
    def __enter__(self):
        try:
            self._conn = psycopg2.connect(user=USERNAME,
                                          password=PASSWORD,
                                          host=HOST,
                                          dbname=DB_NAME)

            self._cur = self._conn.cursor()

            return self

        except Exception as err:
            logging.error(f"DB CONNECTION FAILED: {err}")

    def __exit__(self, *args):
        try:
            self._cur.close()
            self._conn.close()
            logging.debug("Closing connection and cursor...")

        except Exception as err:
            logging.error("DB connection/cursor closing error")

    def execute_query(self, query_str):
        self._cur.execute(query_str)
        return self._cur.fetchall()


    def proto_manage_select(self, func):
        def handle_params(*args):
            def wrapper():
                self._connect()
                self._res = func(*args)
                self._close()
                return self._res
            return wrapper
        return handle_params


if __name__ == '__main__':
    """ 
    DECORATOR BEHAVIOUR PROTOTYPIZATION - 
    just evaluating if could be implemented
    """

    def my_decorator(func):
        def handle_params(something):
            def wrapper():
                print("#TODO CONNECTION...")
                func(something)
                print("#TODO CLOSE ALL...")
            return wrapper
        return handle_params

    @my_decorator
    def foo(what):
        print(f"say something: {what}")

    """
    i_handle_params = my_decorator(foo)

    o_call = i_handle_params("something")

    o_call()
    """

    o = foo("some demo params")
    o()
