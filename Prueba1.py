ingresados =  ["","",""]
def menu():
    print("**menu principal")
    print("1.-Ingresar usuario")
    print("2.-buscar usuario")
    print("3.-Eliminar usuario")
    print("4.- salir")
    opcion = int(input("Imgrese la opcion que quiere usar " ))
    if opcion == 1:
        ingresar()
    elif opcion == 2:
        nombre = input("ingrese el nombre que quiere buscar " )
        buscar(nombre)
    elif opcion == 3:
        nombre = input("ingrese el nombre del usuario que desea eliminar " )
        eliminar(nombre)
    elif opcion == 4:
        salir(opcion)
    else:
        print("debe ingresar un nombre entre 1 y 4")
def ingresar(dato):
    while True:
        for datos in ingresados:
            nombre = input("ingrese el nombre que desea agregar " )
            sexo = input("Ingrese como se edentifica con F , M o C " )
            respuestas = ["F","M","C"]
            contraseña = input("que contraseña quiere poner")
            if sexo.lower() is "f" or "m" or "c":
                (ingresados.insert[nombre], ingresados.insert[sexo], ingresados.insert[contraseña])
                break
            else:
                print(" favor de ingresar bien el sexo ")
def buscar(dato):
    for dato in ingresados[0]:
        nombre = ingresados.__contains__

        print(dato)
def eliminar(nombre):
    for dato in  ingresados[0]:
        nombre = dato[0]
        print(nombre)
        

def salir(opcion):
    print("Cerrando programa....")
menu()
