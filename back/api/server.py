import proc_modules
from flask.json import jsonify
from flask.wrappers import Response
from prometheus_client.exposition import generate_latest
from prometheus_client import Gauge
from flask import Flask, request

procs = proc_modules #PROC_MODULES INSTANCE
app = Flask(__name__)

#PROMETHEUS VARIABLES
gl = Gauge('node_load','load average of number of jobs in the run queue',['duration'])
gu = Gauge('node_uptime','uptime of the system')

#INFORMATION METHODS
#----------------------------------------------------------------------------------            
@app.route('/info/host',methods=['GET'])
def host():
    if request.method == "GET":
        try:
            host = procs.get_hostname()
            return host
        except Exception as e:
            return str(e)

@app.route('/info/uptime',methods=['GET'])
def uptime():
    if request.method == "GET":
        try:
            uptime = procs.get_uptime()
            gu.set(uptime)
            return uptime
        except Exception as e:
            return str(e)

@app.route('/info/load',methods=['GET'])
def load():
    if request.method == "GET":
        try:
            load = procs.get_loadavg()
            l = []
            for v in load.values():
                l.append(v)
            gl.labels(duration="1m").set(l[0])
            gl.labels(duration="5m").set(l[1])
            gl.labels(duration="15m").set(l[2])
            return jsonify(load)
        except Exception as e:
            return str(e)
#METRIC METHOD
#----------------------------------------------------------------------------------            
@app.route('/metrics',methods=['GET'])
def metrics():
    if request.method == "GET":
        try:
            return Response([generate_latest(gl),generate_latest(gu)],mimetype= "text/plain")
        except Exception as e:
            return str(e)
#----------------------------------------------------------------------------------            
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=23333)
