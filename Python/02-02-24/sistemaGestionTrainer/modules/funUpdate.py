import os

from modules.variables import save, getAll, trainers
from modules.funSearch import search

def update():
    os.system("cls")
    print(""" 
        ╔════════════════════╗
        ║ ACTUALIZAR TRAINER ║
        ╚════════════════════╝
    """)
    search()
    
    cod = int(input("Ingrese el codigo del trainer a actualizar: "))
    search(cod)
    op = int(input("""
        Esta seguro que lo quiere editar?
        1. Si
        2. No
        3. Cancelar
    """))
    if(op == 1):
        var = {
            "Codigo": f"{cod}",
            "Nombre" : input("Nombre: "),
            "Apellido" : input("Apellido: "),
            "Edad" : input("Edad: "),
            "Estudios" : input("Estudios: ")
            }
        os.system("pause")
        trainers[cod-1] = var
        
