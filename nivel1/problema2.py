c = int(input("Capital en pesos : "))
x = float(input("Interés : "))
n = int(input("Duration en años : "))

print(str(round(c*(1+x/100)**n, 2)) + " pesos")