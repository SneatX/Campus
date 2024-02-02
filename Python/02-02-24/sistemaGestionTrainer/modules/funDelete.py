import os
from modules.variables import getAll
from modules.funSearch import search

def delete():
    while(True):
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
            os.system("cls")
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
            os.system("pause")
            break
        elif(option == 3):
            break
