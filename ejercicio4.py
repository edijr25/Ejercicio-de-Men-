import os
lista = []

# Función para calcular el total de los números ingresados
def calcular_total():
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        total = sum(lista)
        print("El total de los números ingresados es:", total)

# Función para calcular el promedio de los números ingresados
def calcular_promedio():
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        promedio = sum(lista) / len(lista)
        print("El promedio de los números ingresados es:", promedio)

# Función para obtener el mayor número de la lista
def obtener_mayor():
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        mayor = max(lista)
        print("El número mayor de la lista es:", mayor)

# Función para obtener el menor número de la lista
def obtener_menor():
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        menor = min(lista)
        print("El número menor de la lista es:", menor)

# Función para verificar si un número está en la lista
def verificar_numero():
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        numero = int(input("Ingrese un número: "))
        if numero in lista:
            print("El número", numero, "está en la lista.")
        else:
            print("El número", numero, "no está en la lista.")

# Función para obtener los índices donde aparece un número en la lista
def obtener_indices():
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        numero = int(input("Ingrese un número: "))
        indices = [i for i, x in enumerate(lista) if x == numero]
        if len(indices) == 0:
            print("El número", numero, "no aparece en la lista.")
        else:
            print("El número", numero, "aparece en los índices:", indices)

# Función para contar la cantidad de números pares e impares en la lista
def contar_pares_impares():
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        pares = 0
        impares = 0
        for numero in lista:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        print("La lista contiene", pares, "números pares y", impares, "números impares.")

# Función para contar la cantidad de números positivos, negativos y ceros en la lista
def contar_positivos_negativos_ceros():
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        positivos = 0
        negativos = 0
        ceros = 0
        for numero in lista:
            if numero > 0:
                positivos += 1
            elif numero < 0:
                negativos += 1
            else:
               ceros += 1
        print("La lista contiene", positivos, "números positivos,", negativos, "números negativos y", ceros, "ceros.")


while True:
    print("******Menú*******")
    print("-1 CARGAR LISTA")
    print("-2 TOTAL DE NUM INGRESADOS")
    print("-3 PROMEDIO ")
    print("-4 NUMERO MAYOR")
    print("-5 NUMERO MENOR")
    print("-6 VERIFICAR NUMERO DE LISTA")
    print("-7 INFORMAR INDICE DE NUMERO INGRESADO")
    print("-8 PARES E IMPARES")
    print("-9 POSITIVOS E NEGATIVOS Y CEROS")
    print("-10 VACIAR LISTA")
    print("-11 SALIR")

    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        for i in range(5):
             numeros = int(input("Ingrese un número: "))
             lista.append(numeros)
    
    elif opcion == "2":
        calcular_total()
    
    elif opcion == "3":
        calcular_promedio()
    
    elif opcion == "4":
        obtener_mayor()
    
    elif opcion == "5":
        obtener_menor()
    
    elif opcion == "6":
        verificar_numero ()

    elif opcion == "7":
        obtener_indices()
    
    elif opcion == "8":
        contar_pares_impares()
    
    elif opcion == "9":
        contar_positivos_negativos_ceros()

    elif opcion == "10":
        lista.clear()

    elif opcion == "11":
        salida = input("Confirma salida) s/n:")
        if (salida == "s"):
            break
    else:
        print("Comando incorrecto")
    os.system("pause")
    os.system ("cls")

    