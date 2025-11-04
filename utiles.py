jugadores = []
partidos = []
contador_equipos = 1
contador_jugadores = 1
contador_partidos = 1
equipos = []

def generar_id(tipo):
    global contador_equipos, contador_jugadores, contador_partidos

    if tipo == "equipo":
        id_actual = contador_equipos
        contador_equipos += 1
        return id_actual
    elif tipo == "jugador":
        id_actual = contador_jugadores
        contador_jugadores += 1
        return id_actual
    elif tipo == "partido":
        id_actual = contador_partidos
        contador_partidos += 1
        return id_actual
    else:
        print("El tipo de id no es correcto, tienes que utilizar el tipo equipo, jugador o partido")
        return None

def buscar_equipo_por_id(equipo_id, solo_activos=True):
    for equipo in equipos:
        if equipo["id"] == equipo_id:
            if solo_activos and not equipo["activo"]:
                return None
            return equipo
    return None

def buscar_jugador_por_id(jugador_id, solo_activos=True):
    for jugador in jugadores:
        if jugador["id"] == jugador_id:
            if solo_activos and not jugador["activo"]:
                return None
            return jugador
    return None

def buscar_partido_por_id(partido_id):
    for partido in partidos:
        if partido["id"] == partido_id:
            return partido
    return None
