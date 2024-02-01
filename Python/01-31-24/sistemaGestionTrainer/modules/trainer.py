import os

from modules.variables import save, getAll

def menu():
    opciones = ["Guardar", "Mostrar lista", "Actualizar", "Eliminar", "Salir"]

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
                        #update()
                    case 4:
                        pass
                        #Eliminar ----  Delete
                        delete()
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

def search(codigo = None):

    os.system("cls")

    if (codigo == None):
        print(""" 
        ╔═══════════════════════╗
        ║    Buscar trainers    ║
        ╚═══════════════════════╝   
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
        for i in getAll()[codigo]: 
            print(f"""
        Codigo: {i.get("Codigo")}
        Nombre: {i.get("Nombre")}
        Apellido: {i.get("Apellido")}
        Edad: {i.get("Edad")}
        Estudios: {i.get("Estudios")}
            """)
        os.system("pause")

def delete():
    os.system("cls")
    print(""" 
        ╔═════════════════════════╗
        ║     Eliminar trainer    ║
        ╚═════════════════════════╝   
    """)
    search()

    code = int(input("Ingrese el codigo del trainer que desee eliminar: "))
    search(code)

    option = int(input("""
        Esta segudo que desea eliminar al trainer?

        1. Si
        2. No
        3. Cancelar
                       
        """))
    
    if(option == 1):
        trainerEliminado = getAll().pop(code-1)

        print(f"""
        ╔═════════════════════════╗
        ║    Trainer eliminado    ║
        ╚═════════════════════════╝ 
        Codigo: {trainerEliminado.get("Codigo")}
        Nombre: {trainerEliminado.get("Nombre")}
        Apellido: {trainerEliminado.get("Apellido")}
        Edad: {trainerEliminado.get("Edad")}
        Estudios: {trainerEliminado.get("Estudios")}
        """)

    
    