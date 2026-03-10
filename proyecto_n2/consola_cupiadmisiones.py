#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cupiadmisiones as ca


# Funciones auxiliares (NO MODIFICAR):

def mostrar_candidato(candidato: dict) -> None:
    """
    Muestra los atributos de un candidato en la consola.

    Parámetros:
        candidato (dict): Diccionario con la información del candidato.
    """
    if candidato is not None and candidato != {}:
        print("Nombre:", candidato["nombre"])
        print("Documento de identidad:", candidato["doc_identidad"])
        print("Edad:", candidato["edad"])
        print("Género:", candidato["genero"])
        print("Fecha de postulación:", candidato["fecha_postulacion"])
        print("Nacionalidad:", candidato["nacionalidad"])
        print("Premios académicos:", candidato["num_premios_academicos"])
        print("Puntaje Saber 11°:", candidato["puntaje_saber11"])
        print("Carrera aplicada:", candidato["carrera_aplicada"])
        print("Facultad aplicada:", candidato["facultad_aplicada"])
        print("Tiene discapacidad:", candidato["tiene_discapacidad"])
        print("Es indígena:", candidato["es_indigena"])
        print("Tiene SISBEN:", candidato["tiene_SISBEN"])
        print("Es víctima del conflicto:", candidato["es_victima_conflicto"])
        print("Es becado:", candidato["es_becado"])
        print("Ingresos núcleo familiar:", candidato["ingresos_nucleo_familiar"])
    else:
        print("Error: Candidato inválido.")

# Fin de las funciones auxiliares



# Funciones a implementar (Solo aquellas con TODOs):

def ejecutar_buscar_por_documento(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Ejecuta la búsqueda de un candidato por su documento de identidad.

    Parámetros:
        c1, c2, c3, c4 (dict): Diccionarios con la información de los cuatro candidatos.

    Si se encuentra el candidato, se muestran todos sus datos usando la función auxiliar: `mostrar_candidato()`.
    
    Si no se encuentra, se imprime el mensaje: "No se encontró ningún candidato con ese documento."
    """
    doc = int(input("Ingrese el número de documento de identidad a buscar: "))
    resultado = ca.buscar_candidato_por_doc_identidad(doc, c1, c2, c3, c4)
    if resultado != {}:
        mostrar_candidato(resultado)
    else:
        print("No se encontró ningún candidato con ese documento.")


def ejecutar_filtrar_por_carrera(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Ejecuta el filtrado de candidatos por carrera aplicada.

    Parámetros:
        c1, c2, c3, c4 (dict): Diccionarios con la información de los cuatro candidatos.

    Si hay coincidencias, se imprime:
        "Candidatos que aplicaron a [X]: [Y]"
        
        Donde:
            - [X] es la carrera buscada, ejemplo: "Derecho"
            - [Y] son los documentos de identidad de los candidatos que aplicaron a esa carrera, separados por comas.
        
    Si no hay coincidencias, se imprime:
        "No se encontraron candidatos para la carrera buscada."
    """
    # TODO 9: Implemente la función tal y como se describe en la documentación.
    carrera = input("Ingrese la carrera a buscar: ")
    resultado = ca.filtrar_por_carrera_aplicada(carrera, c1, c2, c3, c4)

    if resultado != "Ninguno":
        print(f"Candidatos que aplicaron a {carrera}: {resultado}")
    else:
        print("No se encontraron candidatos para la carrera buscada.")


def ejecutar_mejor_puntaje_saber11(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Ejecuta la búsqueda del candidato con el mejor puntaje Saber 11°.

    Parámetros:
        c1, c2, c3, c4 (dict): Diccionarios con la información de los cuatro candidatos.

    Se imprime el encabezado: "Candidato con mejor puntaje Saber 11°:"
        Luego se muestran todos los datos del candidato usando la función auxiliar: `mostrar_candidato()`.
    """
    # TODO 10: Implemente la función tal y como se describe en la documentación.
    print("Candidato con mejor puntaje Saber 11°:")
    candidato = ca.mejor_puntaje_saber11(c1, c2, c3, c4)
    mostrar_candidato(candidato)


def ejecutar_postulacion_mas_reciente(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Ejecuta la búsqueda del candidato con la postulación más reciente.

    Parámetros:
        c1, c2, c3, c4 (dict): Diccionarios con la información de los cuatro candidatos.

    Se imprime el encabezado: "Candidato con la postulación más reciente:"
        Luego se muestran todos los datos del candidato usando la función auxiliar: `mostrar_candidato()`.
    """
    # TODO 11: Implemente la función tal y como se describe en la documentación.
    print("Candidato con la postulación más reciente:")
    candidato = ca.postulacion_mas_reciente(c1, c2, c3, c4)
    mostrar_candidato(candidato)


def ejecutar_verificar_saber11_apto(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Ejecuta la verificación de si un candidato tiene un puntaje Saber 11° apto según la facultad.

    Parámetros:
        c1, c2, c3, c4 (dict): Diccionarios con la información de los cuatro candidatos.

    Si el candidato existe (se busca con la función: buscar_candidato_por_doc_identidad), se imprime uno de los siguientes mensajes:
        - "El candidato tiene un puntaje Saber 11° apto."
        - "El candidato NO tiene un puntaje Saber 11° apto."
        
    Si no se encuentra el candidato, se imprime:
        "Candidato no encontrado."
    """
    # TODO 12: Implemente la función tal y como se describe en la documentación.
    doc = int(input("Ingrese el número de documento de identidad del candidato: "))
    candidato = ca.buscar_candidato_por_doc_identidad(doc, c1, c2, c3, c4)

    if candidato != {}:
        if ca.tiene_saber11_apto(candidato):
            print("El candidato tiene un puntaje Saber 11° apto.")
        else:
            print("El candidato NO tiene un puntaje Saber 11° apto.")
    else:
        print("Candidato no encontrado.")


def ejecutar_recomendar_beca(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Ejecuta la recomendación del mejor candidato para una beca del gobierno.

    Parámetros:
        c1, c2, c3, c4 (dict): Diccionarios con la información de los cuatro candidatos.

    Se solicita al usuario un ingreso máximo permitido del núcleo familiar (número entero positivo).

    Si el puntaje de recomendación del mejor candidato es mayor que 0.0,
        Se imprime el encabezado: "Candidato recomendado para la beca:" y luego se muestran sus datos usando la función auxiliar: `mostrar_candidato()`.
        
    Si el puntaje es 0.0, se imprime:
        "Ningún candidato cumple con los requerimientos de la beca."
    """
    # TODO 13: Implemente la función tal y como se describe en la documentación.
    max_ingreso = int(input("Ingrese el ingreso máximo permitido del núcleo familiar: "))
    candidato = ca.recomendar_para_beca(c1, c2, c3, c4, max_ingreso)
    puntaje = ca.puntaje_para_beca_gobierno(candidato, max_ingreso)

    if puntaje > 0.0:
        print("Candidato recomendado para la beca:")
        mostrar_candidato(candidato)
    else:
        print("Ningún candidato cumple con los requerimientos de la beca.")



# Fin de las funciones a implementar


# Funciones del menú:

def imprimir_separador(simbolo: str, repeticiones: int) -> None:
    print(f"{simbolo}" * repeticiones)


def iniciar_aplicacion() -> None:
    """
    Inicializa la aplicación creando cuatro candidatos predefinidos (c1, c2, c3 y c4)
    utilizando la función crear_candidato() de la lógica. 
    
    Cada candidato se crea con los siguientes argumentos, en este orden:

        1. nombre (str):
           Nombre completo del aspirante.

        2. doc_identidad (int):
           Número de documento de identidad del candidato (único).

        3. edad (int):
           Edad del candidato en años.

        4. genero (str):
           Género del candidato (ej. "Masculino", "Femenino").

        5. fecha_postulacion (str):
           Fecha en la que el candidato realizó la postulación, en formato "YYYY-MM-DD".

        6. nacionalidad (str):
           Nacionalidad del aspirante.

        7. num_premios_academicos (int):
           Número de reconocimientos o premios académicos obtenidos.

        8. puntaje_saber11 (int):
           Puntaje global obtenido en la prueba Saber 11°.

        9. carrera_aplicada (str):
           Programa académico al que desea ingresar.

        10. facultad_aplicada (str):
            Facultad a la que pertenece la carrera seleccionada.

        11. tiene_discapacidad (bool):
            Indica si el candidato tiene alguna discapacidad.
            True = Sí, False = No.

        12. es_indigena (bool):
            Indica si pertenece a una comunidad indígena.
            True = Sí, False = No.

        13. tiene_SISBEN (bool):
            Indica si está registrado en el SISBEN.
            True = Sí, False = No.

        14. es_victima_conflicto (bool):
            Indica si es víctima del conflicto armado.
            True = Sí, False = No.

        15. es_becado (bool):
            Indica si cuenta con algún tipo de beca.
            True = Sí, False = No.

        16. ingresos_nucleo_familiar (float):
            Ingresos mensuales del núcleo familiar del candidato.

    Los cuatro candidatos creados son:

        - c1: Eric, aspirante a Medicina.
        - c2: Gabriel, aspirante a Ingeniería Civil.
        - c3: Sofía, aspirante a Biología.
        - c4: Diego, aspirante a Derecho.

    Usted podría cambiar los datos de estos candidatos para hacer más pruebas.
    """
    c1 = ca.crear_candidato("Eric", 101, 18, "Masculino", "2025-06-01", "Colombiana", 2, 375, "Medicina", "Medicina", False, False, True, True, False, 1200000.0)
    c2 = ca.crear_candidato("Gabriel", 102, 19, "Masculino", "2025-06-02", "Peruana", 1, 370, "Ingeniería Civil", "Ingeniería", False, True, False, False, False, 2000000.0)
    c3 = ca.crear_candidato("Sofía", 103, 20, "Femenino", "2025-06-03", "Colombiana", 0, 360, "Biología", "Ciencias", True, False, True, False, True, 900000.0)
    c4 = ca.crear_candidato("Diego", 104, 21, "Masculino", "2025-06-04", "Colombiana", 3, 340, "Derecho", "Derecho", False, False, True, True, False, 1500000.0)

    imprimir_separador("*", 50)
    print("\nBienvenido a CupiAdmisiones\n")
    imprimir_separador("*", 50)
    print("\nCandidatos registrados:\n")
    imprimir_separador("-", 50)
    mostrar_candidato(c1)
    imprimir_separador("-", 50)
    mostrar_candidato(c2)
    imprimir_separador("-", 50)
    mostrar_candidato(c3)
    imprimir_separador("-", 50)
    mostrar_candidato(c4)
    imprimir_separador("-", 50)

    ejecutando = True
    
    while ejecutando:
        ejecutando = mostrar_menu_aplicacion(c1, c2, c3, c4)
        
        if ejecutando:
            input("\nPresione Enter para continuar...")

def mostrar_menu_aplicacion(c1: dict, c2: dict, c3: dict, c4: dict) -> bool:
    """
    Muestra el menú de opciones y ejecuta la opción seleccionada.

    Parámetros:
        c1, c2, c3, c4 (dict): Diccionarios con la información de los cuatro candidatos.

    Retorna:
        bool: True si el programa debe seguir ejecutándose, False para terminar.
    """
    print("\nMenú:")
    print("1 - Buscar candidato por documento de identidad")
    print("2 - Filtrar por carrera aplicada")
    print("3 - Candidato con mejor puntaje Saber 11°")
    print("4 - Candidato con postulación más reciente")
    print("5 - Verificar si el puntaje Saber 11° es apto")
    print("6 - Recomendar candidato para beca")
    print("7 - Salir\n")

    opcion = input("Seleccione una opción: ").strip()
    print("\n" + "-" * 60 + "\n")

    continuar_ejecutando = True

    if opcion == "1":
        ejecutar_buscar_por_documento(c1, c2, c3, c4)
    elif opcion == "2":
        ejecutar_filtrar_por_carrera(c1, c2, c3, c4)
    elif opcion == "3":
        ejecutar_mejor_puntaje_saber11(c1, c2, c3, c4)
    elif opcion == "4":
        ejecutar_postulacion_mas_reciente(c1, c2, c3, c4)
    elif opcion == "5":
        ejecutar_verificar_saber11_apto(c1, c2, c3, c4)
    elif opcion == "6":
        ejecutar_recomendar_beca(c1, c2, c3, c4)
    elif opcion == "7":
        continuar_ejecutando = False
    else:
        print("Opción inválida. Intente nuevamente.")

    return continuar_ejecutando


if __name__ == "__main__":
    iniciar_aplicacion()
    
# Fin de las funciones del menú.
##