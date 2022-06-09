print("Bandera de Inglaterra")
while True:
    L = int(input("Ingrese largo de bandera (L): "))
    H = int(input("Ingrese altura de bandera (H): "))

    if (L%2!=0) and (H%2!=0):
        if ((L<20) and (L>2)) and ((H<20) and (H>2)):
            break
        
columnasI = int( (L - 1)/2 )
columnasD = columnasI

fila_top = ''
for columna in range(columnasI):
    fila_top = fila_top + '0'

fila_top = fila_top + '+'

for columna in range (columnasD):
    fila_top = fila_top + '0'

fila_centro = ''

for columna in range(L):
    fila_centro = fila_centro + '+'

filasArr = int((H-1)/2)
filasAb = filasArr

print('\n')

for fila in range(filasArr):
    print(fila_top)

print(fila_centro)

columnasI = int( (L - 1)/2 )
columnasD = columnasI

fila_botton =''
for columna in range(columnasI):
    fila_botton= fila_botton + '0'

fila_botton = fila_botton + '+'

for columna in range (columnasD):
    fila_botton = fila_botton + '0'

filasArr = int((H-1)/2)
filasAb= filasArr

for fila in range(filasArr):
    print(fila_botton)



