import os
from modules.variables import save, getAll

def create():
    os.system("cls")
    print(""" 
        ╔══════════════════════╗
        ║   AGREGAR TRAINERS   ║
        ╚══════════════════════╝
    """)
    save({
        "Codigo" : (len(getAll()) + 1),
        "Nombre" : input("Nombre: "),
        "Apellido" : input("Apellido: "),
        "Edad" : input("Edad: "),
        "Estudios" : input("Estudios: ")
    })
    os.system("cls")
    print(""" 
          

          


        ╔══════════════════════╗
        ║   Trainer agregado   ║
        ╚══════════════════════╝
          
          
    """)
    os.system("pause")