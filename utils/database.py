import psycopg2
from settings.db_auth import *
import logging
from data.query_tmpls.live_query import *
from utils.db_tools import DbManager


class Database:
    def __init__(self):
        self._conn_manager = DbManager()

    def data_now(self, id_portinformer, states_of_interest):
        query = Q_DATA_NOW.format(id_portinformer=id_portinformer,
                                  states_of_interest=states_of_interest)

        return self._conn_manager.execute_select(query)

    def data_arrival_prev_now(self, id_portinformer):
        query = Q_DATA_ARRIVAL_PREV.format(id_portinformer=id_portinformer)

        return self._conn_manager.execute_select(query)

    def data_shipped_goods_now(self, id_portinformer):
        query = Q_DATA_SHIPPED_GOODS.format(id_portinformer=id_portinformer)

        return self._conn_manager.execute_select(query)

    def data_traffic_list_now(self, id_portinformer):
        query = Q_DATA_TRAFFIC_LIST.format(id_portinformer=id_portinformer)

        return self._conn_manager.execute_select(query)

    def data_static_now(self, id_portinformer, states_of_interest, input_date):
        query = Q_STATIC_DATA.format(id_portinformer=id_portinformer,
                                     states_of_interest=states_of_interest,
                                     input_date=input_date)

        return self._conn_manager.execute_select(query)