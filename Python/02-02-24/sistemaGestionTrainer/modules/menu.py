import os

from modules.variables import save, getAll, guardarJson
from modules.funCreate import create
from modules.funSearch import search
from modules.funDelete import delete
from modules.funUpdate import update


def menu():
    opciones = ["Guardar", "Mostrar lista", "Actualizar", "Eliminar", "Salir"]

    while True:
        os.system("cls")
        print(""" 
            ╔═══════════════════╗
            ║   MENU TRAINERS   ║
            ╚═══════════════════╝
        """)
        for i, item in enumerate (opciones):
            print(f"{i+1}. {item}")

        try:
            option = int(input("-"))
            if(option > 0 and option <= len(opciones)):
                match(option):
                    case 1:
                        #Guardar -----  Create
                        create()
                    case 2:
                        pass
                        #Buscar ------  Get
                        search()
                    case 3:
                        pass
                        #Actualizar --  Update
                        update()
                    case 4:
                        pass
                        #Eliminar ----  Delete
                        delete()
                    case 5:
                        #Salir -------  exit
                        guardarJson()
                        break

        except ValueError:
            print("Incorrect")


    
    