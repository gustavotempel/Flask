from flask import Flask
from flask import request, jsonify
from flask_restful import Resource, Api
import twitter_tools
import csv, json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return 'Hello, World!'

@app.route('/getjson', methods = ['GET', 'POST'])
def getjson():
    return jsonify(
        username = 'Gustavo',
        age = 37,
        email = 'gtempel@hotmail.com'
    )

@app.route('/csv2jsonFile', methods = ['GET','POST'])
def convertCsvJsonFile():
    csvFile = "libro1.csv"
    jsonFile = "libro1.json"

    csvfile = open(csvFile, 'r')
    jsonfile = open(jsonFile, 'w')

    reader = csv.DictReader(csvfile)
    out = json.dumps([row for row in reader], indent = 4)
    jsonfile.write(out)
    return "Convertido!"

@app.route('/csv2json', methods = ['GET','POST'])
def convertCsvJson():
    if request.method == 'POST':
        data = request.data
        #reader = csv.DictReader(data) json.dumps(data)
    return data

@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Pagina no encontrada...</h1>', 404
    
if __name__ == '__main__':
    app.run(debug = True, port = 8000)
