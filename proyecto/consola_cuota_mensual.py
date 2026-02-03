import cupibank as cb


gasto_actual = float(input("Ingrese el gasto actual del cliente: "))
saldo_anterior = float(input("Ingrese el saldo anterior del cliente: "))
numero_pagos = int(input("Ingrese el número de pagos restantes del cliente: "))
print("La cuota mensual del cliente es:", round(cb.calcular_cuota_mensual(gasto_actual, saldo_anterior, numero_pagos), 2))