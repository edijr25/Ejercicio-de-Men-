lista_nota1 = []
lista_nota2 = []
promedio = []

for i in range (3):
    nota1 = int(input("Ingrese la nota del primer parcial: "))
    lista_nota1.append (nota1)

    nota2 = int(input("Ingresa la nota del segundo parcial: "))
    lista_nota2.append (nota2)

    promedio.append ((lista_nota1[i]+ lista_nota2[i])/ 2)

print ("****Lista de notas ***")
print ("Parcial 1      Parcial 2      Promedio")

for i in range (len(lista_nota1)):
    print(f"  {lista_nota1[i]:2d}              {lista_nota2[i]:2d}           {promedio[i]:.2f}")