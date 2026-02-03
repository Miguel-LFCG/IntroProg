import cupibank as cb


salario_base = float(input("Ingrese el salario base del cliente: "))
ingresos_extras = float(input("Ingrese los ingresos extras del cliente: "))
impuestos = float(input("Ingrese los impuestos del cliente: "))
gastos_mensuales = float(input("Ingrese los gastos mensuales del cliente: "))
porcentaje_endeudamiento = float(input("Ingrese el porcentaje de endeudamiento permitido : "))
confiabilidad = float(input("Ingrese la confiabilidad del cliente : "))
referidos = int(input("Ingrese el número de referidos del cliente: "))
riesgo = float(input("Ingrese el riesgo del cliente : "))
print("El cupo límite del cliente es:", round(cb.calcular_cupo_limite(salario_base, ingresos_extras, impuestos, gastos_mensuales, porcentaje_endeudamiento, confiabilidad, referidos, riesgo), 2))