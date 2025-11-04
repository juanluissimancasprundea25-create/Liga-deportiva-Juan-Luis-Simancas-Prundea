import utiles

def registrar_resultado():
    print("\n--- Registrar resultado ---")
    partidos_pendientes = [p for p in utiles.partidos if not p["jugado"]]
    if not partidos_pendientes:
        print("No hay partidos pendientes")
        return
    print("\nLos partidos pendientes son:")
    filas = []
    
    for p in partidos_pendientes:
        local = utiles.buscar_equipo_por_id(p["local_id"], solo_activos=False)
        visitante = utiles.buscar_equipo_por_id(p["visitante_id"], solo_activos=False)
        local_nombre = local["nombre"] if local else "Desconocido"
        visitante_nombre = visitante["nombre"] if visitante else "Desconocido"
        filas.append([p["id"], p["jornada"], local_nombre, visitante_nombre, p["fecha"]])
    print(filas)
    id_partido = int(input("\nEscribe el id del partido: "))
    if id_partido is None:
        print("El id tiene que ser un numero")
        return
    partido = utiles.buscar_partido_por_id(id_partido)
    if partido is None:
        print("No existe ese partido")
        return
    if partido["jugado"]:
        print("Este partido ya tiene un resultado")
        return
    goles_local = int(input("Escribe los goles del equipo que juega: "))
    if goles_local is None:
        print("Los goles deben ser un numero mayor o igual a 0")
        return
    goles_visitante = int(input("Escribe los goles del equipo al que se enfrentan: "))
    if goles_visitante is None:
        print("Los goles deben ser un numero mayor o igual a 0")
        return
    partido["resultado"] = f"{goles_local}-{goles_visitante}"
    partido["jugado"] = True
    local = utiles.buscar_equipo_por_id(partido["local_id"], solo_activos=False)
    visitante = utiles.buscar_equipo_por_id(partido["visitante_id"], solo_activos=False)
    print(f"\nLos resultados del partido son : {local['nombre']} {goles_local} - {goles_visitante} {visitante['nombre']}")

def calcular_estadisticas_equipo(equipo_id):
    stats = {"PJ": 0, "G": 0, "E": 0, "P": 0, "GF": 0, "GC": 0, "DG": 0, "PTS": 0}
    for partido in utiles.partidos:
        if partido["jugado"]:
            es_local = partido["local_id"] == equipo_id
            es_visitante = partido["visitante_id"] == equipo_id
            if es_local or es_visitante:
                resultado = partido["resultado"].split("-")
                goles_local = int(resultado[0])
                goles_visitante = int(resultado[1])
                stats["PJ"] += 1
                if es_local:
                    stats["GF"] += goles_local
                    stats["GC"] += goles_visitante
                    if goles_local > goles_visitante:
                        stats["G"] += 1
                        stats["PTS"] += 3
                    elif goles_local == goles_visitante:
                        stats["E"] += 1
                        stats["PTS"] += 1
                    else:
                        stats["P"] += 1
                else:
                    stats["GF"] += goles_visitante
                    stats["GC"] += goles_local
                    if goles_visitante > goles_local:
                        stats["G"] += 1
                        stats["PTS"] += 3
                    elif goles_visitante == goles_local:
                        stats["E"] += 1
                        stats["PTS"] += 1
                    else:
                        stats["P"] += 1
    stats["DG"] = stats["GF"] - stats["GC"]
    return stats

def mostrar_clasificacion():
    print("\n--- Clasificacion ---")
    clasificacion = []
    for equipo in utiles.equipos:
        if equipo["activo"]:
            stats = calcular_estadisticas_equipo(equipo["id"])
            clasificacion.append({"nombre": equipo["nombre"], "PJ": stats["PJ"], "G": stats["G"], "E": stats["E"], "P": stats["P"], "GF": stats["GF"], "GC": stats["GC"], "DG": stats["DG"], "PTS": stats["PTS"]})
    if not clasificacion:
        print("No hay equipos o no se han jugado partidos")
        return
    clasificacion.sort(key=lambda x: (-x["PTS"], -x["DG"], -x["GF"]))
    filas = []
    for i, equipo in enumerate(clasificacion, 1):
        filas.append([i, equipo["nombre"], equipo["PJ"], equipo["G"], equipo["E"], equipo["P"], equipo["GF"], equipo["GC"], equipo["DG"], equipo["PTS"]])
    print(filas)

def estadisticas_por_equipo():
    print("\n--- Estadisticas por equipo ---")
    id_equipo = int(input("Escribe el id del equipo: "))
    if id_equipo is None:
        print("El ID tiene que ser un numero")
        return
    equipo = utiles.buscar_equipo_por_id(id_equipo, solo_activos=True)
    if equipo is None:
        print("Ese equipo no existe o no esta activo")
        return
    stats = calcular_estadisticas_equipo(id_equipo)
    print(f"Estadisticas de: {equipo['nombre']}")
    print(f"Partidos jugados: {stats['PJ']}")
    print(f"Ganados: {stats['G']}")
    print(f"Empatados: {stats['E']}")
    print(f"Perdidos: {stats['P']}")
    print(f"Goles a favor: {stats['GF']}")
    print(f"Goles en contra: {stats['GC']}")
    print(f"Diferencia de goles: {stats['DG']:+d}")
    print(f"Puntos: {stats['PTS']}")

def menu_resultados():
    salir = False
    while not salir:
        print("--- Resultados o clasificacion ---")
        print("1. Registrar resultado de partido")
        print("2. Ver clasificacion general")
        print("3. Ver estadísticas de un equipo")
        print("4. Volver")
        opcion = input("Elige una de las opciones: ")
        
        if opcion == "1":
            registrar_resultado()
        elif opcion == "2":
            mostrar_clasificacion()
        elif opcion == "3":
            estadisticas_por_equipo()
        elif opcion == "4":
            salir = True
        else:
            print("Esa opcion no existe")
