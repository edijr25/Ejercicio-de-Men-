import os

while True:

    print("***Menú de opciones***")
    print("-----------------------")
    print("1- Saludar")
    print("2- Despedir")
    print("3- Brindar")
    print ("4- Limpiar terminal")
    print("5- Salir")

    opcion = input("Ingrese una opción: ")

    
    if opcion == "1":
        print("Hola")
    elif opcion == "2":
        print("Adios")
    elif opcion == "3":
        print("Salud")
    elif opcion == "5":
        break
    elif opcion == "4":
        os.system("cls")
    else:
        print("Comando incorrecto")