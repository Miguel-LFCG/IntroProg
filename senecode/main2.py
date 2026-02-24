


def mejor_del_salon(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5):
    m_estudiante1 = {"nombre": estudiante1["nombre"],"promedio" : (estudiante1["matematicas"] + estudiante1["español"] + estudiante1["ciencias"] + estudiante1["literatura"] + estudiante1["arte"])/5}
    m_estudiante2 = {"nombre": estudiante2["nombre"],"promedio" : (estudiante2["matematicas"] + estudiante2["español"] + estudiante2["ciencias"] + estudiante2["literatura"] + estudiante2["arte"])/5}
    m_estudiante3 = {"nombre": estudiante3["nombre"],"promedio" : (estudiante3["matematicas"] + estudiante3["español"] + estudiante3["ciencias"] + estudiante3["literatura"] + estudiante3["arte"])/5}
    m_estudiante4 = {"nombre": estudiante4["nombre"],"promedio" : (estudiante4["matematicas"] + estudiante4["español"] + estudiante4["ciencias"] + estudiante4["literatura"] + estudiante4["arte"])/5}
    m_estudiante5 = {"nombre": estudiante5["nombre"],"promedio" : (estudiante5["matematicas"] + estudiante5["español"] + estudiante5["ciencias"] + estudiante5["literatura"] + estudiante5["arte"])/5}

    result = m_estudiante1
    if result["promedio"] < m_estudiante2["promedio"]:
        result = m_estudiante2
    if result["promedio"] < m_estudiante3["promedio"]:
        result = m_estudiante3
    if result["promedio"] < m_estudiante4["promedio"]:
        result = m_estudiante4
    if result["promedio"] < m_estudiante5["promedio"]:
        result = m_estudiante5

    return result["nombre"]

def mejor_de_cada_curso(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5):
    def comparar(materia, e1, e2):
        if e1[materia] > e2[materia]:
            return e1
        elif e1[materia] < e2[materia]:
            return e2
        else:
            if e1["nombre"] < e2["nombre"]:
                return e1
            else:
                return e2

    def obtener_mejor(materia):
        mejor = comparar(materia, estudiante1, estudiante2)
        mejor = comparar(materia, mejor, estudiante3)
        mejor = comparar(materia, mejor, estudiante4)
        mejor = comparar(materia, mejor, estudiante5)
        return mejor["nombre"]

    return {
        "matematicas": obtener_mejor("matematicas"),
        "español": obtener_mejor("español"),
        "ciencias": obtener_mejor("ciencias"),
        "literatura": obtener_mejor("literatura"),
        "arte": obtener_mejor("arte")
    }



def suficientes_uvas(cantidad_ivan: int, cantidad_nicolas: int, cantidad_adriana: int, cantidad_verde: int, cantidad_morada: int, cantidad_negra: int)->str:
    """ ¿Suficientes Uvas?
    Parámetros:
      cantidad_ivan (int): La cantidad de uvas que Iván desea comer
      cantidad_nicolas (int): La cantidad de uvas que Nicolás desea comer
      cantidad_adriana (int): La cantidad de uvas que Adriana desea comer
      cantidad_verde (int): La cantidad de uvas verdes de las que disponen los amigos
      cantidad_morada (int): La cantidad de uvas moradas de las que disponen los amigos
      cantidad_negra (int): La cantidad de uvas negras de las que disponen los amigos
    Retorno:
      str: La función retorna "felices", si todos los amigos pueden comer la cantidad de uvas que quieren;
           "casi", si dos de los 3 amigos pueden comer la cantidad de uvas que quieren; "fallamos", si
           solamente 1 amigo puede comer la cantidad de uvas que quiere; "al menos somos amigos", si ninguno de
           los amigos puede comer la cantidad de uvas que quiere.
    """
    can_i = cantidad_ivan <= cantidad_verde
    can_n = cantidad_nicolas <= cantidad_verde + cantidad_morada
    can_a = cantidad_adriana <= cantidad_verde + cantidad_morada + cantidad_negra
    
    can_in = can_i and (cantidad_ivan + cantidad_nicolas <= cantidad_verde + cantidad_morada)
    can_ia = can_i and (cantidad_ivan + cantidad_adriana <= cantidad_verde + cantidad_morada + cantidad_negra)
    can_na = can_n and (cantidad_nicolas + cantidad_adriana <= cantidad_verde + cantidad_morada + cantidad_negra)
    
    can_ina = can_in and (cantidad_ivan + cantidad_nicolas + cantidad_adriana <= cantidad_verde + cantidad_morada + cantidad_negra)
    
    if can_ina:
        return "felices"
    elif can_in or can_ia or can_na:
        return "casi"
    elif can_i or can_n or can_a:
        return "fallamos"
    else:
        return "al menos somos amigos"