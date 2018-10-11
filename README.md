# The Dude [WIP]
Web services - Sanic rulez 

**Python Dook's porting**

Shipreporting BI service based on Python/uvloop/asyncio/async-await


![the Dude](https://i.imgur.com/UjgpSVB.jpg)


**Description**

webservice consumed by Shipreporting client - live and historical data exposed via REST APIs

**Usage**

```bash
$ pipenv --python 3.7
$ pipenv install -r requirements.txt
$ pipenv shell
$ python app.py

[201X-XX-XX 17:56:35 +0200] [20892] [INFO] Goin' Fast @ http://0.0.0.0:8000
[201X-XX-XX 17:56:35 +0200] [20896] [INFO] BOOTSTRAPING...
[201X-XX-XX 17:56:35 +0200] [20896] [INFO] BOOTSTRAP COMPLETED!
[201X-XX-XX 17:56:35 +0200] [20896] [INFO] Starting worker [XXXXXX]


$ curl -i http://127.0.0.1:8000/get_roadstead_now/28
HTTP/1.1 200 OK
Connection: keep-alive
Keep-Alive: 5
Content-Length: 323
Content-Type: application/json

[SHIPPING DATA OUTPUT OMITTED]

```

**Exposed APIs**


**REAL TIME DATA:**

|API | URL | Description|
|:----|:-----|:------------|
|Moored now|/api/moored_now/:id_portinformer/|Get portinformer's currently moored|
|At roadstead now|/api/roadstead_now/:id_portinformer/|Get portinformer's currently at roadstead|
|Arrivals|/api/arrivals_now/:id|Get portinformer's arrivals today| 
|Departures|/api/departures_now/:id    | Get portinformer's departures today| 
|Arrival previsions today|/api/arrival_previsions_now/:id    |Get portinformer's arrival previsions  |
|Traffic list|/api/traffic_list_now/:id    |Get portinformer's traffic list data   |
|Commercial operations|/api/shipped_goods_now/:id    |Get portinformer's shipped goods data    |


**ARCHIVE DATA:**

|API | URL | Description|
|:----|:-----|:------------|
|Moored|/api/moored/:start/:stop/:id_portinformer/|Get portinformer moored|
|At roadstead|/api/roadstead/:start/:stop/:id_portinformer/|Get portinformer at roadstead|
|Arrival previsions|    |    |
|Arrivals|    |    | 
|Departures|    |    | 
|Traffic list|    |    |
|Commercial operations|    |    |
