def encontrar_ganador_beca(estudiante1: dict, estudiante2: dict, estudiante3: dict, estudiante4: dict)->str:
    """ Ganador de la CupiBeca
    Parámetros:
      estudiante1 (dict): Diccionario con los datos del primer estudiante
      estudiante2 (dict): Diccionario con los datos del segundo estudiante
      estudiante3 (dict): Diccionario con los datos del tercer estudiante
      estudiante4 (dict): Diccionario con los datos del cuarto estudiante
    Retorno:
      str: Mensaje indicando el resultado de la selección del ganador de la beca.
    """
    total1 = estudiante1["matematicas"] + estudiante1["lenguaje"] + estudiante1["ingles"] + estudiante1["ciencias"] + estudiante1["sociales"]
    total2 = estudiante2["matematicas"] + estudiante2["lenguaje"] + estudiante2["ingles"] + estudiante2["ciencias"] + estudiante2["sociales"]
    total3 = estudiante3["matematicas"] + estudiante3["lenguaje"] + estudiante3["ingles"] + estudiante3["ciencias"] + estudiante3["sociales"]
    total4 = estudiante4["matematicas"] + estudiante4["lenguaje"] + estudiante4["ingles"] + estudiante4["ciencias"] + estudiante4["sociales"]

    mayor_puntaje = total1
    ganador = estudiante1["nombre"]
    hay_empate = False

    if total2 > mayor_puntaje:
      mayor_puntaje = total2
      ganador = estudiante2["nombre"]
      hay_empate = False
    elif total2 == mayor_puntaje:
      hay_empate = True

    if total3 > mayor_puntaje:
      mayor_puntaje = total3
      ganador = estudiante3["nombre"]
      hay_empate = False
    elif total3 == mayor_puntaje:
      hay_empate = True

    if total4 > mayor_puntaje:
      mayor_puntaje = total4
      ganador = estudiante4["nombre"]
      hay_empate = False
    elif total4 == mayor_puntaje:
      hay_empate = True

    if hay_empate:
      return "Hay un empate. Los estudiantes deberán someterse a un CupiTest para definir al ganador."

    return "El ganador de la CupiBeca es: " + str(ganador)



def encriptar_mensaje(mensaje: str)->str:
    """ Encriptador de mensajes
    Parámetros:
      mensaje (str): Mensaje que se debe encriptar
    Retorno:
      str: Mensaje encriptado siguiendo las reglas especificadas
    """
    if "aa" in mensaje or "ae" in mensaje or "ai" in mensaje or "ao" in mensaje or "au" in mensaje:
      mensaje = mensaje.replace("a", "-")

    if "x" in mensaje:
      mensaje = "Cupi2" + mensaje.replace("x", "")

    if "i" not in mensaje:
      mensaje = mensaje.upper()
      mensaje = mensaje.replace("A", "V")
      mensaje = mensaje.replace("E", "V")
      mensaje = mensaje.replace("I", "V")
      mensaje = mensaje.replace("O", "V")
      mensaje = mensaje.replace("U", "V")

    if "seneca" in mensaje:
      mensaje = mensaje.swapcase()

    return mensaje