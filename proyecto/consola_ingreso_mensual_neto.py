import cupibank as cb

salario_base = float(input("Salario base : "))
ingresos_extras = float(input("Ingresos extras : "))
impuestos = float(input("Impuestos : "))

print("El ingreso mensual neto es: ", round(cb.ingreso_mensual_neto(salario_base, ingresos_extras, impuestos), 2))