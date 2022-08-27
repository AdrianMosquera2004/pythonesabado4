observador=100

print("**Menu**")
print("0.Salir")
print("1.Saludar")
print("2.Despedir")
while(observador != 0):
    observador=int(input("Digite una opcion: "))
    if(observador==0):
        break
    elif(observador==1):
        print("Hola")
    elif(observador==2):
        print("chao")
    else:
        print("Digite una opcion valida")        