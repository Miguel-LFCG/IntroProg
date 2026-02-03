

#Calcula los ingresos disponibles del cliente después de deducciones.
def ingreso_mensual_neto(salario_base, ingresos_extras, impuestos):
    return (salario_base + ingresos_extras) - (impuestos + salario_base*0.037 + salario_base*0.045)


#Calcula el monto máximo que el cliente puede destinar a deudas.
def capacidad_de_eudeudamiento(salario_base, ingresos_extras, impuestos, gastos_mensuales, porcentaje_endeudamiento):
    return (ingreso_mensual_neto(salario_base, ingresos_extras, impuestos) - gastos_mensuales)*porcentaje_endeudamiento

#Evalúa la solvencia del cliente según confiabilidad, referidos y riesgo.
def calcular_calificacion_crediticia(confiabilidad, referidos, riesgo):
    peso_confiabilidad = 0.5
    beneficio_por_referido = 0.1
    return ((confiabilidad*peso_confiabilidad)+(referidos*beneficio_por_referido))/riesgo

#Calcula el monto máximo de crédito que puede otorgarse al cliente.
def calcular_cupo_limite(salario_base, ingresos_extras, impuestos, gastos_mensuales, porcentaje_endeudamiento, confiabilidad, referidos, riesgo):
    return capacidad_de_eudeudamiento(salario_base, ingresos_extras, impuestos, gastos_mensuales, porcentaje_endeudamiento)*calcular_calificacion_crediticia(confiabilidad, referidos,riesgo)

#Calcula cuánto debe pagarse cada mes según gastos y deuda pendiente.
def calcular_cuota_mensual(gasto_actual, saldo_anterior, numero_pagos):
    tasa_interes_mensual = 0.025
    return gasto_actual+((saldo_anterior*tasa_interes_mensual*(1+tasa_interes_mensual)**numero_pagos)/((1+tasa_interes_mensual)**numero_pagos) -1)



