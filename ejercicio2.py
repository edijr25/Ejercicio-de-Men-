import os

flag_saludo = False
flag_brindis = False

while True:
    os.system ("cls")
    print("***Menú de opciones***")
    print("-----------------------")
    print("1- Saludar")
    print("2- Brindar")
    print("3- Despedir")
    print("4- Salir")

    opcion = input("Ingrese una opción: ")

    
    if opcion == "1":
        print("Hola")
        flag_saludo = True
    
    elif opcion == "2":
        if flag_saludo == True:
            print("Salud")
            flag_brindis = True
        else:
            print("Antes de brindar saludame")

    elif opcion == "3":
        if flag_brindis == True:
            print("Adios")
            flag_saludo =False
            flag_brindis = False
        elif flag_saludo== True:
            print("Antes de despedirno primero brindemos")
        else:
            print("Antes de despedirnos primero saludame")
    
    
    elif opcion == "4":
        salida = input("Confirma salida) s/n:")
        if (salida == "s"):
            break
    else:
        print("Comando incorrecto")

    os.system("pause")