import cupibank as cb

salario_base = float(input("Salario base : "))
ingresos_extras = float(input("Ingresos extras : "))
impuestos = float(input("Impuestos : "))
gastos_mensuales = float(input("Gastos mensuales : "))
porcentaje_endeudamiento = float(input("Porcentaje de endeudamiento permitido (en decimal) : "))

print("La capacidad de endeudamiento es: ", round(cb.capacidad_de_eudeudamiento(salario_base, ingresos_extras, impuestos, gastos_mensuales, porcentaje_endeudamiento), 2))