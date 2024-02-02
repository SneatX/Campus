import json

datosCamper = [{
    "Nombre" : "Santiago",
    "Apellido" : "Ospina"
}]

convertirJson = json.dumps(datosCamper, indent = 4)

with open("data.json" , "w+") as f:
    f.write(convertirJson)
    f.close()
    