import json
import os

trainers = []

def save(data):
    trainers.append(data)

def getAll(code = None):
    if(code == None):
        return trainers
    else:
        return trainers[code-1]
    
    
def guardarJson():
    with open("Python/02-02-24/sistemaGestionTrainer/data/data.json" , "w") as file:
        json.dump(trainers, file, indent = 4)
        file.close()
        
def tomarJson():
    with open("Python/02-02-24/sistemaGestionTrainer/data/data.json", "r") as archivo:
        trainers = json.loads(archivo.read())
tomarJson()