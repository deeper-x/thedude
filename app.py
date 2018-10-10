import os

from sanic import Sanic
from sanic.log import logger as log
from sanic import response
from sanic.exceptions import ServerError
from utils.database import Database
from settings.data import *
app = Sanic(__name__)


@app.route("/get_moored_now/<id_portinformer:int>")
def get_moored_now(request, id_portinformer):
    obj_db = Database()
    res = obj_db.data_now(id_portinformer, STATES_OF_MOORING)
    obj_db.close()

    return response.json(res)


@app.route("/get_roadstead_now/<id_portinformer:int>")
def get_roadstead_now(request, id_portinformer):
    obj_db = Database()
    res = obj_db.data_now(id_portinformer, STATES_OF_ROADSTEAD)
    obj_db.close()

    return response.json(res)


@app.route("/get_arrival_previsions_now/<id_portinformer:int>")
def get_arrival_previsions(request, id_portinformer):
    obj_db = Database()
    res = obj_db.data_arrival_prev(id_portinformer)
    obj_db.close()

    return response.json(res)


@app.route("/get_shipped_goods_now/<id_portinformer:int>")
def get_shipped_goods_now(request, id_portinformer):
    obj_db = Database()
    res = obj_db.data_shipped_goods(id_portinformer)
    obj_db.close()

    return response.json(res)


@app.route("/get_traffic_list_now/<id_portinformer:int>")
def get_traffic_list_now(request, id_portinformer):
    obj_db = Database()
    res = obj_db.data_traffic_list_now(id_portinformer)
    obj_db.close()

    return response.json(res)


@app.route("/get_arrivals_now/<id_portinformer:int>/<year:int>/<month:int>/<day:int>")
def get_arrivals_now(request, id_portinformer, year, month, day):
    input_date = f"{year}-{month}-{day}"
    obj_db = Database()
    res = obj_db.data_static_now(id_portinformer, STATES_OF_ARRIVALS, input_date)
    obj_db.close()

    return response.json(res)


@app.route("/get_departures_now/<id_portinformer:int>/<year:int>/<month:int>/<day:int>")
def get_departures_now(request, id_portinformer, year, month, day):
    input_date = f"{year}-{month}-{day}"
    obj_db = Database()
    res = obj_db.data_static_now(id_portinformer, STATES_OF_DEPARTURES, input_date)
    obj_db.close()

    return response.json(res)


# RUNNING SERVER CALLS #
@app.listener('before_server_start')
def before_start(app, loop):
    log.info("BOOTSTRAPING...")


@app.listener('after_server_start')
def after_start(app, loop):
    log.info("BOOTSTRAP COMPLETED!")


@app.listener('before_server_stop')
def before_stop(app, loop):
    log.info("SERVER CLOSING")


@app.listener('after_server_stop')
def after_stop(app, loop):
    log.info("SERVER PROCESS CLOSED")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
