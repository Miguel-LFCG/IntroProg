import cupibank as cb


confiabilidad = float(input("Ingrese la confiabilidad del cliente : "))
referidos = int(input("Ingrese el número de referidos del cliente: "))
riesgo = float(input("Ingrese el riesgo del cliente : "))
print("La calificación crediticia del cliente es:", round(cb.calcular_calificacion_crediticia(confiabilidad, referidos, riesgo), 2))