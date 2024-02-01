import os

from .variables import save 

def menu():
    opciones = ["Guardar", "Buscar", "Actualizar", "Eliminar", "Salir"]

    while True:
        os.system("clear")
        print(""" 
            ╔═══════════════════╗
            ║   MENU TRAINERS   ║
            ╚═══════════════════╝
        """)
        for i, item in enumerate (opciones):
            print(f"{i+1}. {item}")

        try:
            option = int(input("-"))
            if(option > 0 and opcion <= len(opciones)):
                match(option):
                    case 1:
                        #Guardar -----  Create
                        create()
                    case 2:
                        pass
                        #Buscar ------  Get
                        #read()
                    case 3:
                        pass
                        #Actualizar --  Update
                        #update()
                    case 4:
                        pass
                        #Eliminar ----  Delete
                        #delete()
                    case 5:
                        #Salir -------  exit
                        break

        except ValueError:
            print("Incorrect")

def create():
    os.system("cls")
    print(""" 
        ╔══════════════════════╗
        ║   AGREGAR TRAINERS   ║
        ╚══════════════════════╝
    """)
    save({
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



            