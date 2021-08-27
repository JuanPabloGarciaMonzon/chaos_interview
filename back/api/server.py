from flask import Flask, request,jsonify
import json
import proc_modules
global aws
from flask_cors import CORS
 
procs = proc_modules
app = Flask(__name__)
CORS(app)

# #HEALTH CHECK
# @app.route('/',methods=['GET'])
# def root():
#     print("soy python")
#     return "python"

#PROC METRICS
@app.route('/host',methods=['GET'])
def host():
    if request.method == "GET":
        try:
            host = procs.get_hostname()
            return jsonify(host)
        except Exception as e:
            exp = e
            print(exp)
            return "0"

@app.route('/uptime',methods=['GET'])
def uptime():
    if request.method == "GET":
        try:
            uptime = procs.get_uptime()
            return jsonify(uptime)
        except Exception as e:
            exp = e
            print(exp)
            return "0"

@app.route('/load',methods=['GET'])
def load():
    if request.method == "GET":
        try:
            load = procs.get_loadavg()
            return jsonify(load)
        except Exception as e:
            exp = e
            print(exp)
            return "0"

if __name__ == '__main__':
    app.run(host="0.0.0.0")