entero = input("Ingrese un numero entero: ")

try:
    entero = int(entero)
    print "El numero que usted ingreso fue: ", entero

except ValueError:
    print "Error inesperado"
finally:
    print "Thanks"



