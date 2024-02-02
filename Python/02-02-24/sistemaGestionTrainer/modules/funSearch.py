import os

from modules.variables import getAll

def search(codigo = None):

    os.system("cls")

    if (codigo == None):
        print(""" 
        ╔═════════════════╗
        ║     trainers    ║
        ╚═════════════════╝   
        """)
        for i in getAll(): 
            print(f"""
        Codigo: {i.get("Codigo")}
        Nombre: {i.get("Nombre")}
        Apellido: {i.get("Apellido")}
        Edad: {i.get("Edad")}
        Estudios: {i.get("Estudios")}
            """)
        os.system("pause")

    else:        
        val = getAll(codigo)
        print(f"""
        Codigo: {val.get("Codigo")}
        Nombre: {val.get("Nombre")}
        Apellido: {val.get("Apellido")}
        Edad: {val.get("Edad")}
        Estudios: {val.get("Estudios")}
        """)
        os.system("pause")