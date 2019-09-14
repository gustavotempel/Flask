import json

openfile = open("jsonload/data.json", "r")
readfile = openfile.read()
datasource = json.loads(readfile)

sourceresults = datasource['results']['sourceresults']

persona = sourceresults['persona']
personaFisica = sourceresults['personaFisica']
direccion = sourceresults['direccion']
solicitudes = sourceresults['solicitudes']
morosidades = sourceresults['morosidades']