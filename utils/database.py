import psycopg2
from config.db_auth import *
import logging
from data.query_tmpls.live_query import *


class Database:
    def __init__(self):
        try:
            self._conn = psycopg2.connect(user=USERNAME,
                                          password=PASSWORD,
                                          host=HOST,
                                          dbname=DB_NAME)
            self._cur = self._conn.cursor()

        except Exception as err:
            logging.error("DB CONNECTION FAILED")

    def data_now(self, id_portinformer, states_of_interest):
        self._cur.execute(Q_DATA_NOW.format(id_portinformer=id_portinformer,
                                            states_of_interest=states_of_interest))

        return self._cur.fetchall()

    def data_arrival_prev_now(self, id_portinformer):
        self._cur.execute(Q_DATA_ARRIVAL_PREV.format(id_portinformer=id_portinformer))

        return self._cur.fetchall()

    def data_shipped_goods_now(self, id_portinformer):
        self._cur.execute(Q_DATA_SHIPPED_GOODS.format(id_portinformer=id_portinformer))

        return self._cur.fetchall()

    def data_traffic_list_now(self, id_portinformer):
        self._cur.execute(Q_DATA_TRAFFIC_LIST.format(id_portinformer=id_portinformer))

        return self._cur.fetchall()

    def data_static_now(self, id_portinformer, states_of_interest, input_date):
        self._cur.execute(Q_STATIC_DATA.format(id_portinformer=id_portinformer,
                                               states_of_interest=states_of_interest,
                                               input_date=input_date))

        return self._cur.fetchall()


    def close(self):
        self._cur.close()
        self._conn.close()
