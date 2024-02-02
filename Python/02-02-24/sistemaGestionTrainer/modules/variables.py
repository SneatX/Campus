import json

def save(data):
    trainers.append(data)

def getAll(code = None):
    if(code == None):
        return trainers
    else:
        return trainers[code]
    
def guardarJson():
    with open("data.json" , "w") as file:
        json.dump(trainers, file, indent = 4)
        
# def tomarJson():
#     with open("data.json", "r") as archivo:
#         archivo.read()

trainers = []


     
