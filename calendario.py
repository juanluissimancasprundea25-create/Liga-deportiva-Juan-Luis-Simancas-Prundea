import datetime
import utiles

def crear_partido():
    print("\n--- Crear partido ---")
    
    jornada = int(input("Escribe el numero de la partida siendo mayor o igual a uno: "))
    if jornada is None:
        print("La jornada tiene que ser mayor o igual a 1")
        return
    local_id = int(input("Escribe el id del equipo que va a jugar: "))
    if local_id is None:
        print("El id tiene que ser un numero")
        return
    visitante_id = int(input("Escribe el id del equipo que se va a enfrentar: "))
    if visitante_id is None:
        print("El id tiene que ser un numero")
        return
    if local_id == visitante_id:
        print("Un equipo no puede enfrentarse a si mismo")
        return
    equipo_local = utiles.buscar_equipo_por_id(local_id, solo_activos=True)
    equipo_visitante = utiles.buscar_equipo_por_id(visitante_id, solo_activos=True)
    if equipo_local is None or equipo_visitante is None:
        print("Ambos equipos deben existir y estar activos")
        return
    fecha = input("Escribe la fecha del partido en el formato DD-MM-YYYY: ")
    hora = input("Escribe la hora del partido en el formato HH-MM: ")
    try:
        datetime.datetime.strptime(fecha, "%d-%m-%Y")
        datetime.datetime.strptime(hora, "%H:%M")
    except ValueError:
        print("El formato de la hora o fecha no es correcta")
        return
    for p in utiles.partidos:
        if p["jornada"] == jornada:
            if (p["local_id"] == local_id and p["visitante_id"] == visitante_id) or \
               (p["local_id"] == visitante_id and p["visitante_id"] == local_id):
                print("Ese partido ya existe en esta jornada")
                return
    partido = {"id": utiles.generar_id("partido"), "jornada": jornada, "local_id": local_id, "visitante_id": visitante_id, "fecha": fecha, "hora": hora, "jugado": False, "resultado": None}
    utiles.partidos.append(partido)
    print(f"Hemos creado el partido : {equipo_local['nombre']} vs {equipo_visitante['nombre']} con id (ID: {partido['id']})")

def listar_partidos():
    print("\n--- Listar partidos ---")
    print("1. Todos los partidos")
    print("2. Por jornada")
    opcion = input("Elige una de las opciones: ")
    lista = []
    if opcion == "1":
        lista = utiles.partidos
    elif opcion == "2":
        jornada = int(input("Escribe el numero de la jornada: "))
        if jornada is None:
            print("La jornada tiene que ser un número")
            return
        lista = [p for p in utiles.partidos if p["jornada"] == jornada]
    else:
        print("Esa opcion no existe")
        return
    if not lista:
        print("No hay partidos")
        return
    filas = []
    
    for p in lista:
        local = utiles.buscar_equipo_por_id(p["local_id"], solo_activos=False)
        visitante = utiles.buscar_equipo_por_id(p["visitante_id"], solo_activos=False)
        local_nombre = local["nombre"] if local else "Desconocido"
        visitante_nombre = visitante["nombre"] if visitante else "Desconocido"
        estado = "Sí" if p["jugado"] else "No"
        resultado = p["resultado"] if p["resultado"] else "-"
        filas.append([p["id"], p["jornada"], local_nombre, visitante_nombre, p["fecha"], p["hora"], estado, resultado])
    print(filas)

def reprogramar_partido():
    print("\n--- Reprogramar partido ---")
    
    id_partido = int(input("Escribe el id del partido que quieres reprogramar: "))
    if id_partido is None:
        print("El id tiene que ser un numero")
        return
    partido = utiles.buscar_partido_por_id(id_partido)
    if partido is None:
        print("No existe ese partido")
        return
    if partido["jugado"]:
        print("No se puede reprogramar un partido ya jugado")
        return
    fecha = input("Escribe la nueva fecha del partido en formato DD-MM-YYYY: ")
    hora = input("Escribe la nueva hora del partido en formato HH:MM : ")
    try:
        datetime.datetime.strptime(fecha, "%d-%m-%Y")
        datetime.datetime.strptime(hora, "%H:%M")
    except ValueError:
        print("El formato de la hora o fecha no es correcta")
        return
    partido["fecha"] = fecha
    partido["hora"] = hora
    print("Hemos creado el partido")

def eliminar_partido():
    print("\n--- Eliminar partido ---")
    
    id_partido = int(input("Escribe el id del partido que quieres eliminar o activar: "))
    if id_partido is None:
        print("El id tiene que ser un numero")
        return
    partido = utiles.buscar_partido_por_id(id_partido)
    if partido is None:
        print("No existe ese partido")
        return
    if partido["jugado"]:
        print("No se puede eliminar un partido ya jugado")
        return
    str(input("Si quieres eliminar este partido escribe s :"))
    utiles.partidos.remove(partido)
    print("Hemos eliminado este partido")

def menu_partidos():
    salir = False
    while not salir:
        print("--- Menu del calendario de partidos ---")
        print("1. Crear partido")
        print("2. Listar partidos")
        print("3. Reprogramar partido")
        print("4. Eliminar partido")
        print("5. Volver")
        opcion = input("Elige una de las opciones ")
        
        if opcion == "1":
            crear_partido()
        elif opcion == "2":
            listar_partidos()
        elif opcion == "3":
            reprogramar_partido()
        elif opcion == "4":
            eliminar_partido()
        elif opcion == "5":
            salir = True
        else:
            print("Esa opcion no existe")
