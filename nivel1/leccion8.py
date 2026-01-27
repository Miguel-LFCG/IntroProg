#Defina una función que convierta grados Fahrenheit en grados centígrados. 
#Para calcular los grados centígrados debe restar 32 a los grados Fahrenheit y multiplicar el resultado por cinco novenos.


def fahrenheit_a_centigrados(fahrenheit):
    return (fahrenheit - 32)*5/9

#print(fahrenheit_a_centigrados(32))


#Defina una función que convierta grados centígrados en grados Fahrenheit.

def centigrados_a_fahrenheit(centigrados):
    return (centigrados* 9/5)+32

#print(centigrados_a_fahrenheit(0))

#Defina una función que convierta radianes en grados. Recuerde que 360 grados son 2π radianes.
#360 grados = 2π radianes


def radianes_a_grados(radianes):
    return radianes * 180

#print(radianes_a_grados(2))


#Defina una función que convierta grados en radianes.

def grados_a_radianes(grados):
    return grados/180

#print(grados_a_radianes(360))

#Defina una función que reciba un número entero positivo de 4 cifras (dígitos) y devuelva el número invertido.

def invertido(n):
    n1 = int(n/1000)
    n2 = int(n/100) - n1 *10
    n3 = int(n/10) - n1 * 100 - n2 * 10
    n4 = n - n1 * 1000 - n2 * 100 - n3 *10
    return str(n4)+str(n3)+str(n2)+str(n1)

print(invertido(3456))