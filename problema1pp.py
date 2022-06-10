print("Problema 1 Practica de GEOLOGIA")
numDias = 0
numDiasError = 0
numErroresMin = 0
numErroresMax = 0
numErroresT = 0
variacionesMax = 0
variacionesMin = 0
entrada = input("Ingrese resultados de la medicion separados con un espacio y luego enter, marque (0 0) para terminar: ").split(sep=' ', maxsplit=1)
entrada1 = int(entrada[0])
entrada2 = int(entrada[1])
while entrada1 != 0 or entrada2 != 0:
    numDias+= 1
    error1 = False
    error2 = False
    if entrada1<0 or entrada1>50 or entrada2<0 or entrada2>50:
        numDiasError+= 1
        if entrada1>100 or entrada2>100:
            numErroresMax+= 1
            error1 = True
            numErroresT+= 1
        if entrada1<-100 or entrada2<-100:
            numErroresMin+= 1
            error2 = True
            numErroresT+= 1
    if entrada1>=0 and entrada1<=50:
        variacionesMax = variacionesMax + entrada1
    if entrada2>=0 and entrada2<=50:
        variacionesMin = variacionesMin + entrada2
    entrada = input("Ingrese resultados de la medicion separados con un espacio y luego enter, marque (0 0) para terminar: ").split(sep=' ', maxsplit=1)
    entrada1 = int(entrada[0])
    entrada2 = int(entrada[1])
print("Dias totales de campo: ", numDias)
print("Dias con mediciones con errores: ", numDiasError)
print("Errores de medicion gravimetricas mayores a 100: ",numErroresMax)
print("Errores de medicion gravimetrica menores a -100: ",numErroresMin)
print("Errores por ambos: ",numErroresT)
variacionesMax = variacionesMax/numDias
variacionesMin = variacionesMin/numDias
print("Media maxima: ",variacionesMax)
print("Media minima: ",variacionesMin)
