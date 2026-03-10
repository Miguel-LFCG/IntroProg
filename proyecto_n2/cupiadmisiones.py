#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def crear_candidato(
    nombre: str,
    doc_identidad: int,
    edad: int,
    genero: str,
    fecha_postulacion: str,
    nacionalidad: str,
    num_premios_academicos: int,
    puntaje_saber11: int,
    carrera_aplicada: str,
    facultad_aplicada: str,
    tiene_discapacidad: bool,
    es_indigena: bool,
    tiene_SISBEN: bool,
    es_victima_conflicto: bool,
    es_becado: bool,
    ingresos_nucleo_familiar: float
) -> dict:
    """
    Crea y retorna un diccionario que representa un candidato a ingresar a la universidad con todos sus atributos requeridos.

    Las llaves del diccionario retornado coinciden exactamente con los nombres de los parámetros.

    Parámetros:
        nombre (str): Nombre completo del candidato. Ejemplo: "Zutano Mengano".
        doc_identidad (int): Número de documento de identidad. Ejemplo: 1023456789.
        edad (int): Edad del candidato en años. Ejemplo: 18.
        genero (str): Género del candidato. Ejemplo: "Masculino".
        fecha_postulacion (str): Fecha de postulación en formato "YYYY-MM-DD". Ejemplo: "2025-06-21".
        nacionalidad (str): Nacionalidad del candidato. Ejemplo: "Colombiana".
        num_premios_academicos (int): Número de premios académicos obtenidos. Ejemplo: 3.
        puntaje_saber11 (int): Puntaje global obtenido en la prueba Saber 11°. Ejemplo: 351.
        carrera_aplicada (str): Carrera universitaria a la que aplica. Ejemplo: "Ingeniería Civil".
        facultad_aplicada (str): Facultad correspondiente a la carrera. Ejemplo: "Ingeniería".
        tiene_discapacidad (bool): Indica si el candidato tiene alguna discapacidad.
        es_indigena (bool): Indica si el candidato pertenece a una comunidad indígena.
        tiene_SISBEN (bool): Indica si el candidato está registrado en el SISBEN.
        es_victima_conflicto (bool): Indica si el candidato es víctima del conflicto armado.
        es_becado (bool): Indica si el candidato cuenta con alguna beca.
        ingresos_nucleo_familiar (float): Ingresos mensuales del núcleo familiar. Ejemplo: 1500000.0

    Retorna:
        dict: Diccionario que representa al candidato, con las llaves coincidiendo con los nombres de los parámetros.
    """
    # TODO 1: Implemente la función tal y como se describe en la documentación.
    return {
        "nombre": nombre,
        "doc_identidad": doc_identidad,
        "edad": edad,
        "genero": genero,
        "fecha_postulacion": fecha_postulacion,
        "nacionalidad": nacionalidad,
        "num_premios_academicos": num_premios_academicos,
        "puntaje_saber11": puntaje_saber11,
        "carrera_aplicada": carrera_aplicada,
        "facultad_aplicada": facultad_aplicada,
        "tiene_discapacidad": tiene_discapacidad,
        "es_indigena": es_indigena,
        "tiene_SISBEN": tiene_SISBEN,
        "es_victima_conflicto": es_victima_conflicto,
        "es_becado": es_becado,
        "ingresos_nucleo_familiar": ingresos_nucleo_familiar,
    }


def buscar_candidato_por_doc_identidad(doc_buscado: int, c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    """
    Retorna el diccionario del candidato cuyo número de documento de identidad coincida exactamente con el valor buscado.

    Parámetros:
        doc_buscado (int): Número exacto de documento de identidad a buscar.
        c1 (dict): Diccionario que representa al primer candidato.
        c2 (dict): Diccionario que representa al segundo candidato.
        c3 (dict): Diccionario que representa al tercer candidato.
        c4 (dict): Diccionario que representa al cuarto candidato.

    Retorna:
        dict: Diccionario correspondiente al candidato con documento coincidente o diccionario vacío si no hay coincidencia.
    """
    # TODO 2: Implemente la función tal y como se describe en la documentación.
    if c1["doc_identidad"] == doc_buscado:
        return c1
    if c2["doc_identidad"] == doc_buscado:
        return c2
    if c3["doc_identidad"] == doc_buscado:
        return c3
    if c4["doc_identidad"] == doc_buscado:
        return c4

    return {}


def filtrar_por_carrera_aplicada(carrera_buscada: str, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Filtra los candidatos cuya carrera aplicada coincide exactamente con la carrera buscada.
    Retorna una cadena con los documentos de identidad de los candidatos filtrados, separados por comas.

    Parámetros:
        carrera_buscada (str): Nombre exacto de la carrera a buscar. Ejemplo: "Medicina".
        c1 (dict): Diccionario que representa al primer candidato.
        c2 (dict): Diccionario que representa al segundo candidato.
        c3 (dict): Diccionario que representa al tercer candidato.
        c4 (dict): Diccionario que representa al cuarto candidato.

    Retorna:
        str: Cadena con los documentos de identidad de los candidatos filtrados o "Ninguno" si no hay coincidencias.
    """
    # TODO 3: Implemente la función tal y como se describe en la documentación.
    documentos = ""

    if c1["carrera_aplicada"] == carrera_buscada:
        documentos = str(c1["doc_identidad"])

    if c2["carrera_aplicada"] == carrera_buscada:
        if documentos == "":
            documentos = str(c2["doc_identidad"])
        else:
            documentos += ", " + str(c2["doc_identidad"])

    if c3["carrera_aplicada"] == carrera_buscada:
        if documentos == "":
            documentos = str(c3["doc_identidad"])
        else:
            documentos += ", " + str(c3["doc_identidad"])

    if c4["carrera_aplicada"] == carrera_buscada:
        if documentos == "":
            documentos = str(c4["doc_identidad"])
        else:
            documentos += ", " + str(c4["doc_identidad"])

    if documentos == "":
        return "Ninguno"

    return documentos


def mejor_puntaje_saber11(c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    """
    Retorna el diccionario del candidato con el mayor puntaje en la prueba Saber 11°.

    Parámetros:
        c1 (dict): Diccionario que representa al primer candidato.
        c2 (dict): Diccionario que representa al segundo candidato.
        c3 (dict): Diccionario que representa al tercer candidato.
        c4 (dict): Diccionario que representa al cuarto candidato.

    Retorna:
    dict: Diccionario correspondiente al candidato con el mayor puntaje obtenido en la prueba Saber 11°,
        En caso de empate, retorna el último candidato que alcanza ese puntaje en el orden c1 a c4.
    """
    # TODO 4: Implemente la función tal y como se describe en la documentación.
    mejor = c1

    if c2["puntaje_saber11"] >= mejor["puntaje_saber11"]:
        mejor = c2
    if c3["puntaje_saber11"] >= mejor["puntaje_saber11"]:
        mejor = c3
    if c4["puntaje_saber11"] >= mejor["puntaje_saber11"]:
        mejor = c4

    return mejor


def postulacion_mas_reciente(c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    """
    Retorna el diccionario del candidato con la fecha de postulación más reciente.

    Nota:
        Las fechas de postulación ("fecha_postulacion") están en el formato "YYYY-MM-DD" (Año-Mes-Día).
    
        En Python, este formato permite que las fechas puedan compararse directamente como strings, 
        ya que el orden lexicográfico coincide con el orden cronológico.
    
        Ejemplos de comparaciones:
            "2005-02-15" < "2006-06-10"  # → True (Porque 2005 es anterior a 2006)
            "2010-08-23" > "2009-12-31"  # → True (Porque 2010 es posterior a 2009)
            "2015-03-10" < "2015-03-20"  # → True (Mismo año y mes, pero el día 10 es anterior al día 20)

    Parámetros:
        c1 (dict): Diccionario que representa al primer candidato.
        c2 (dict): Diccionario que representa al segundo candidato.
        c3 (dict): Diccionario que representa al tercer candidato.
        c4 (dict): Diccionario que representa al cuarto candidato.

    Retorna:
    dict: Diccionario correspondiente al candidato con la fecha más reciente de postulación.
        En caso de empate, se retorna el primer candidato que tenga dicha fecha en el orden c1 a c4.
    """
    # TODO 5: Implemente la función tal y como se describe en la documentación.
    mas_reciente = c1

    if c2["fecha_postulacion"] > mas_reciente["fecha_postulacion"]:
        mas_reciente = c2
    if c3["fecha_postulacion"] > mas_reciente["fecha_postulacion"]:
        mas_reciente = c3
    if c4["fecha_postulacion"] > mas_reciente["fecha_postulacion"]:
        mas_reciente = c4

    return mas_reciente


def tiene_saber11_apto(candidato: dict) -> bool:
    """
    Determina si el candidato tiene un puntaje Saber 11° igual o superior al mínimo requerido según la facultad a la que aplica.
    Los puntajes mínimos son determinados por el siguiente listado de facultades:
        - Artes y Humanidades: 345 puntos.
        - Ciencias Sociales: 345 puntos.
        - Derecho: 350 puntos.
        - Economía: 350 puntos.
        - Administración: 355 puntos.
        - Ciencias: 360 puntos.
        - Ingeniería: 370 puntos.
        - Medicina: 375 puntos.
        
    Parámetros:
        candidato (dict): Diccionario que representa al candidato, con los campos "facultad_aplicada" y "puntaje_saber11".

    Retorna:
        bool: True si el puntaje Saber 11° es suficiente para la facultad correspondiente, False en caso contrario.
    """
    # TODO 6: Implemente la función tal y como se describe en la documentación.
    puntajes_minimos = {
        "Artes y Humanidades": 345,
        "Ciencias Sociales": 345,
        "Derecho": 350,
        "Economía": 350,
        "Administración": 355,
        "Ciencias": 360,
        "Ingeniería": 370,
        "Medicina": 375,
    }

    facultad = candidato["facultad_aplicada"]
    if facultad not in puntajes_minimos:
        return False

    return candidato["puntaje_saber11"] >= puntajes_minimos[facultad]


def puntaje_para_beca_gobierno(candidato: dict, max_ingreso_nucleo_familiar: float) -> float:
    """
    Calcula un puntaje para aspirar a una beca del gobierno colombiano con base en ciertas condiciones.
    
    Hay dos casos generales:
        
    1. Si el candidato no tiene el puntaje Saber 11° mínimo requerido para ser admitido a la facultad que aplica o ya es becado, el puntaje es 0.0.
    
    2. Caso contrario, se suman 0.2 puntos por cada condición que se cumpla:
      - Nacionalidad es "Colombiana".
      - Tiene más de 0 premios académicos.
      - Está registrado en el SISBEN.
      - Es víctima del conflicto.
      - Ingresos del núcleo familiar son menores o iguales al máximo permitido.

    Parámetros:
        candidato (dict): Diccionario que representa al candidato.
        max_ingreso_nucleo_familiar (float): Valor máximo permitido de ingresos familiares mensuales.

    Retorna:
        float: Puntaje entre 0.0 y 1.0 de elegibilidad para beca del gobierno colombiano, redondeado a 2 decimales.
    """
    # TODO 7: Implemente la función tal y como se describe en la documentación.
    if not tiene_saber11_apto(candidato) or candidato["es_becado"]:
        return 0.0

    puntaje = 0.0
    if candidato["nacionalidad"] == "Colombiana":
        puntaje += 0.2
    if candidato["num_premios_academicos"] > 0:
        puntaje += 0.2
    if candidato["tiene_SISBEN"]:
        puntaje += 0.2
    if candidato["es_victima_conflicto"]:
        puntaje += 0.2
    if candidato["ingresos_nucleo_familiar"] <= max_ingreso_nucleo_familiar:
        puntaje += 0.2

    return round(puntaje, 2)


def recomendar_para_beca(c1: dict, c2: dict, c3: dict, c4: dict, max_ingreso_nucleo_familiar: float) -> dict:
    """
    Evalúa cuatro candidatos y retorna aquel con el mayor puntaje para ser recomendado a una beca del gobierno colombiano.

    Parámetros:
        c1 (dict): Primer candidato.
        c2 (dict): Segundo candidato.
        c3 (dict): Tercer candidato.
        c4 (dict): Cuarto candidato.
        max_ingreso_nucleo_familiar (float): Ingreso máximo del núcleo familiar para sumar puntos.

    Retorna:
        dict: Candidato con mayor prioridad para recibir una beca del gobierno colombiano.
            En caso de empate en puntaje, se prioriza por mayor puntaje obtenido en la prueba Saber 11°.
                Si persiste el empate, se prioriza por mayor cantidad de premios académicos.
                   Si aún persiste, se retorna el primero en el orden c1 a c4.
    """
    # TODO 8: Implemente la función tal y como se describe en la documentación.
    mejor_candidato = c1
    mejor_puntaje = puntaje_para_beca_gobierno(c1, max_ingreso_nucleo_familiar)
    puntaje_c2 = puntaje_para_beca_gobierno(c2, max_ingreso_nucleo_familiar)
    if puntaje_c2 > mejor_puntaje:
        mejor_candidato = c2
        mejor_puntaje = puntaje_c2
    elif puntaje_c2 == mejor_puntaje:
        if c2["puntaje_saber11"] > mejor_candidato["puntaje_saber11"]:
            mejor_candidato = c2
            mejor_puntaje = puntaje_c2
        elif c2["puntaje_saber11"] == mejor_candidato["puntaje_saber11"]:
            if c2["num_premios_academicos"] > mejor_candidato["num_premios_academicos"]:
                mejor_candidato = c2
                mejor_puntaje = puntaje_c2

    puntaje_c3 = puntaje_para_beca_gobierno(c3, max_ingreso_nucleo_familiar)
    if puntaje_c3 > mejor_puntaje:
        mejor_candidato = c3
        mejor_puntaje = puntaje_c3
    elif puntaje_c3 == mejor_puntaje:
        if c3["puntaje_saber11"] > mejor_candidato["puntaje_saber11"]:
            mejor_candidato = c3
            mejor_puntaje = puntaje_c3
        elif c3["puntaje_saber11"] == mejor_candidato["puntaje_saber11"]:
            if c3["num_premios_academicos"] > mejor_candidato["num_premios_academicos"]:
                mejor_candidato = c3
                mejor_puntaje = puntaje_c3

    puntaje_c4 = puntaje_para_beca_gobierno(c4, max_ingreso_nucleo_familiar)
    if puntaje_c4 > mejor_puntaje:
        mejor_candidato = c4
        mejor_puntaje = puntaje_c4
    elif puntaje_c4 == mejor_puntaje:
        if c4["puntaje_saber11"] > mejor_candidato["puntaje_saber11"]:
            mejor_candidato = c4
            mejor_puntaje = puntaje_c4
        elif c4["puntaje_saber11"] == mejor_candidato["puntaje_saber11"]:
            if c4["num_premios_academicos"] > mejor_candidato["num_premios_academicos"]:
                mejor_candidato = c4
                mejor_puntaje = puntaje_c4

    return mejor_candidato

