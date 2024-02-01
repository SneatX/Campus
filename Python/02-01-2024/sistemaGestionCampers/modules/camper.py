import os
from .variables import save, getAll, camper

def create():
    os.system('cls')
    print(f"""
          {'-'*20}
          Formulario de Camper
          {'-'*20}""")
    save({
        "Nombre": input("Nombre: "),
        "Apellido": input("Apellido: "),
        "Edad": input("Edad: "),
        "Genero": input ("Genero: ")
    })
    os.system('pause')

def read(codigo = None):
    os.system("clear")
    print("""
    *************************
    *    Tabla de campers   *
    *************************
    """)
    if(codigo == None):
        for i, val in enumerate(getAll()):
            print(f"""
            --------------------------------
            Codigo: {i+1}
            Nombre: {val.get("Nombre")}
            Apellido: {val.get("Apellido")}
            Edad: {val.get("Edad")}
            Genero: {val.get("Genero")}
            --------------------------------
            """)
    else:
        val = getAll()[codigo-1]
        print(f"""
        --------------------------------
        Codigo: {codigo}
        Nombre: {val.get("Nombre")}
        Apellido: {val.get("Apellido")}
        Edad: {val.get("Edad")}
        Genero: {val.get("Genero")}
        --------------------------------
        """)
    os.system("pause")

def update():
    bandera = True
    while (bandera):
        os.system('clear')
        read()
        print("""
        ***************************
        *   Actualizar un camper  *
        ***************************
        """)
        codigo = int(input("Codigo del camper a actualizar: "))
        read(codigo)
        print("""
        Esta seguro que desea actualizar un camper?
        1. Si
        2. No
        3. Cancelar
        """)
        opc = int(input())
        match(opc):
            case 1:
                val = {
                    "Nombre": input("Nombre: "),
                    "Apellido": input("Apellido: "),
                    "Edad": input("Edad: "),
                    "Genero": input ("Genero: ")
                }
                camper[codigo-1] = val
                os.system("clear")
                print(f"""
                Camper Actualizado
                --------------------------------
                Codigo: {codigo}
                Nombre: {val.get("Nombre")}
                Apellido: {val.get("Apellido")}
                Edad: {val.get("Edad")}
                Genero: {val.get("Genero")}
                --------------------------------
                """)
                os.system("pause")
                bandera = False
            case 3:
                bandera = False

def delete():
    bandera = True
    while (bandera):
        os.system('clear')
        read()
        print("""
        *************************
        *   Eliminar un camper  *
        *************************
        """)
        codigo = int(input("Codigo del camper a eliminar: "))
        read(codigo)
        print("""
        Esta seguro que desea eliminar un camper?
        1. Si
        2. No
        3. Cancelar
        """)

        opc = int(input())
        match(opc):
            case 1:
                val = camper.pop(codigo-1)
                os.system("clear")
                print(f"""
                Camper eliminado
                --------------------------------
                Codigo: {codigo}
                Nombre: {val.get("Nombre")}
                Apellido: {val.get("Apellido")}
                Edad: {val.get("Edad")}
                Genero: {val.get("Genero")}
                --------------------------------
                """)
                os.system("pause")
                bandera = False
            case 3:
                bandera = False

def menu():

    menu = ['Guardar', 'Buscar', 'Actualizar', 'Eliminar', 'Salir']
    while True:
        os.system('cls')
        print(f"""
        {'-'*12}
        Menú Camper
        {'-'*12}""")
        print(''.join([f'{item+1}. {value}\n' for item, value in enumerate(menu)]))
        try:
            option = int(input('Option: '))
            if option <= len(menu) and option > 0:
                match(option):
                    case 1:
                        create()
                    case 2:
                        read()
                    case 3:
                        update()
                    case 4:
                        delete()
                    case 5:
                         break
        except ValueError:
            print('Choose a option')

