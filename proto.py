from sanic import Sanic
from sanic.log import logger as log
from sanic import response
from utils.database import Database

app = Sanic(__name__)


@app.route("/proto_query")
def query_string(request):
    return response.json({"parsed": True, "args": request.args, "url": request.url,
                          "query_string": request.query_string})


@app.route("/dynamic/<name>/<i:int>")
def test_params(request, name, i):
    return response.text("yeehaww {} {}".format(name, i))


@app.route("/query_string")
def query_string(request):
    return response.json({"parsed": True, "args": request.args, "url": request.url,
                          "query_string": request.query_string})


@app.route("/async_await")
async def test_await(request):
    import asyncio
    await asyncio.sleep(5)
    return response.text("request completed async...")


@app.route("/get_moored_now/<id_portinformer:int>")
def get_moored_now(request, id_portinformer):
    obj_db = Database()
    return response.text("request completed!")






## RUNNING SERVER CALLS ##
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
