import numpy as np

Lista = []
contador = 0
while True:
    numero = int(input("Ingrese un valor y presione 0 para finalizar: "))

    if numero == 0:
        break
    Lista.append(numero)    
contador = len(Lista)
if contador <20:
     print('Digite una lista de cifras mayor o igual a 20 numeros. Reinicie el programa. ')
media = np.mean(Lista)
mediana = np.median(Lista)
desvist = np.std(Lista)
minimo = np.min(Lista)
maximo = np.max(Lista)

print(f"Los datos ingresados fueron los siguientes: {Lista}")
print(f"El valor de la media es: {media}")
print(f"El valor de la mediana es: {mediana}")
print(f"El valor de la Desviacion estandar es: {desvist}")
print(f"El Rango es:( {minimo} , {maximo} )")
