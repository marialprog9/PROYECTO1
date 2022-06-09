Retiro = int(input("Ingrese la cantidad a retirar: "))

if Retiro >= 100:
    saldo = Retiro // 100
    print(str(saldo)+ (' Billete'if Retiro >= 100 else ' Billetes') +( 's' if saldo>= 1 else '' )+ " de 100$")
    Retiro = Retiro % 100
if  Retiro >= 50:
    saldo = Retiro // 50
    print(str(saldo)+ (' Billete'if Retiro >= 50 else ' Billetes') +( 's' if saldo> 1 else '' )+ " de 50$")
    Retiro = Retiro % 50   
if Retiro >= 20:
    saldo = Retiro // 20
    print(str(saldo)+ (' Billete'if Retiro >= 20 else ' Billetes')+( 's' if saldo> 1 else '' ) + " de 20$")
    Retiro = Retiro % 20    
if Retiro >= 10:
    saldo = Retiro // 10
    print(str(saldo)+ (' Billete'if Retiro >= 10 else ' Billetes') +( 's' if saldo> 1 else '' )+ " de 10$")
    Retiro = Retiro % 10
if Retiro >= 5:
    saldo = Retiro // 5
    print(str(saldo)+ (' Billete'if Retiro >= 5 else ' Billetes') +( 's' if saldo> 1 else '' )+ " de 5$")
    Retiro = Retiro % 5
if Retiro >= 1:
    saldo = Retiro // 1
    print(str(saldo)+ (' Billete'if Retiro >= 1 else ' Billetes') +( 's' if saldo> 1 else '' )+ " de 1$")
    Retiro = Retiro % 1
