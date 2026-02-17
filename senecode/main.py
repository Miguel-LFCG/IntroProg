def responder_saludo(mensaje: str)->str:
    """ Clasificador de saludos automáticos
    Parámetros:
      mensaje (str): Cadena que representa un posible saludo informal.
    Retorno:
      str: Respuesta automática correspondiente al saludo.
    """
    if mensaje.lower() == "hola":
        return "¡Hola! ¿Cómo estás?"
    elif mensaje.lower() == "hello":
        return "Hello! How are you?"
    elif mensaje.lower() == "hi":
        return "Hi there!"
    elif mensaje.lower() == "qué más":
        return "¡Quiubo!"
    elif mensaje.lower() == "saludos":
        return "¡Saludos cordiales!"
    else:
        return "No reconozco el saludo."
    

def estado_academico(nota1: float, creditos1: int, nota2: float, creditos2: int, nota3: float, creditos3: int, nota4: float, creditos4: int, nota5: float, creditos5: int, nota6: float, creditos6: int)->str:
    """ Estado académico
    Parámetros:
      nota1 (float): Nota del curso 1 (entre 0 y 5.0)
      creditos1 (int): La cantidad de créditos asignados al curso 1
      nota2 (float): Nota del curso 2 (entre 0 y 5.0)
      creditos2 (int): La cantidad de créditos asignados al curso 2
      nota3 (float): Nota del curso 3 (entre 0 y 5.0)
      creditos3 (int): La cantidad de créditos asignados al curso 3
      nota4 (float): Nota del curso 4 (entre 0 y 5.0)
      creditos4 (int): La cantidad de créditos asignados al curso 4
      nota5 (float): Nota del curso 5 (entre 0 y 5.0)
      creditos5 (int): La cantidad de créditos asignados al curso 5
      nota6 (float): Nota del curso 6 (entre 0 y 5.0)
      creditos6 (int): La cantidad de créditos asignados al curso 6
    Retorno:
      str: Estado académico del estudiante según su promedio ('SUSPENDIDO', 'PRUEBA' o 'NORMAL')
    """
    promedio_ponderado = round((nota1 * creditos1 + nota2 * creditos2 + nota3 * creditos3 + nota4 * creditos4 + nota5 * creditos5 + nota6 * creditos6) / (creditos1 + creditos2 + creditos3 + creditos4 + creditos5 + creditos6), 2)
    
    if promedio_ponderado < 3.0:
        return "SUSPENDIDO"
    elif 3.0 <= promedio_ponderado < 3.25:
        return "PRUEBA"
    else:
        return "NORMAL"
    

def conteo_buenas_notas(notas: dict)->int:
    """ Materias Excepcionales
    Parámetros:
      notas (dict): Diccionario con las notas del estudiante
    Retorno:
      int: Número de materias excepcionales, es decir, aquellas con calificación estrictamente superior a 4.
    """
    count = 0
    if notas["Matematica"] > 4:
        count += 1
    if notas["Ingles"] > 4:
        count += 1
    if notas["Sociales"] > 4:
        count += 1
    if notas["Ciencias"] > 4:
        count +=1
    if notas["Deportes"] > 4:
        count +=1
    return count

notas = {

    "Matematica": 5,
    "Ingles": 2,
    "Sociales": 4,
    "Ciencias": 2,
    "Deportes": 5


}

#print(conteo_buenas_notas(notas))

def calcular_precio_pasaje(temporada: str, compania: str, edad: int, estudiante: bool)->int:
    """ Precio de un Pasaje
    Parámetros:
      temporada (str): Cadena que indica la temporada, puede ser "ALTA" o "BAJA"
      compania (str): Cadena que indica la compañía con la que se hace el vuelo, puede ser "ALAS" o "VOLAR"
      edad (int): Edad del pasajero
      estudiante (bool): True en caso que el pasajero sea estudiante, False de lo Contrario
    Retorno:
      int: Precio calculado del pasaje Bogotá-Tokio según los parámetros
    """
    tarifa_base = 5000000
    porcentaje = 0
    
    if temporada == "ALTA":
        if compania == "ALAS":
            porcentaje += 30
        elif compania == "VOLAR":
            porcentaje += 20
    
    if edad < 18:
        porcentaje -= 50
    
    if edad > 60 and compania == "VOLAR":
        porcentaje += 0
    
    if estudiante and compania == "ALAS" and edad >= 18 and temporada == "BAJA":
        porcentaje -= 10
    
    precio = tarifa_base + tarifa_base * porcentaje / 100
    
    if edad > 60 and compania == "VOLAR":
        precio += 100000
    
    return int(precio)


def contar_picas(numero_secreto: int, numero_propuesto: int)->int:
    """ Picas y Fijas: contar picas
    Parámetros:
      numero_secreto (int): Número que se debe adivinar
      numero_propuesto (int): Número propuesto para tratar de adivinar el número secreto
    Retorno:
      int: Cantidad de picas que hay en el número propuesto (dígitos en la posición incorrecta)
    """
    digit1_s = numero_secreto // 1000
    digit2_s = (numero_secreto // 100) % 10
    digit3_s = (numero_secreto // 10) % 10
    digit4_s = numero_secreto % 10
    digit1_p = numero_propuesto // 1000
    digit2_p = (numero_propuesto // 100) % 10
    digit3_p = (numero_propuesto // 10) % 10
    digit4_p = numero_propuesto % 10
    picas = 0
    if digit1_s != digit1_p:
        if digit1_p == digit2_s or digit1_p == digit3_s or digit1_p == digit4_s:
            picas += 1
    if digit2_s != digit2_p:
        if digit2_p == digit1_s or digit2_p == digit3_s or digit2_p == digit4_s:
            picas += 1
    if digit3_s != digit3_p:
        if digit3_p == digit1_s or digit3_p == digit2_s or digit3_p == digit4_s:
            picas += 1
    if digit4_s != digit4_p:
        if digit4_p == digit1_s or digit4_p == digit2_s or digit4_p == digit3_s:
            picas += 1

    return picas

#print(contar_picas(3222, 4321))
