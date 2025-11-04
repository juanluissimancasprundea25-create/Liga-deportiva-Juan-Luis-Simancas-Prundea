import utiles

def crear_jugador():
    print("\n--- Crear jugador ---")
    
    nombre = str(input("Escribe el nombre del jugador: "))
    if nombre is None:
        print("El nombre no puede estar vacio")
        return
    posicion = str(input("Escribe la posición del jugador: "))
    if posicion is None:
        print("La posicion no puede estar vacio")
        return
    equipo_id = int(input("Escribe el id del equipo: "))
    if equipo_id is None:
        print("El id tiene que ser un numero")
        return
    equipo = utiles.buscar_equipo_por_id(equipo_id, solo_activos=True)
    if equipo is None:
        print("Ese equipo no existe o no esta activo")
        return
    jugador = {"id": utiles.generar_id("jugador"), "nombre": nombre, "posicion": posicion, "equipo_id": equipo_id, "activo": True}
    utiles.jugadores.append(jugador)
    print(f"Hemos creado al jugador '{nombre}' con id {jugador['id']} en el equipo '{equipo['nombre']}'")

def listar_jugadores():
    print("\n--- Listar jugadores ---")
    print("1. Todos los jugadores")
    print("2. Jugadores de equipo")
    opcion = input("Elige una de las opciones: ")
    lista = []
    if opcion == "1":
        lista = [j for j in utiles.jugadores if j["activo"]]
    elif opcion == "2":
        equipo_id = int(input("Escribe el id del equipo: "))
        if equipo_id is None:
            print("El id del equipo debe ser un numero")
            return
        lista = [j for j in utiles.jugadores if j["equipo_id"] == equipo_id and j["activo"]]
    else:
        print("Esa opcion no existe")
        return
    if not lista:
        print("No hay jugadores")
        return
    
    filas = []
    
    for j in lista:
        equipo = utiles.buscar_equipo_por_id(j["equipo_id"], solo_activos=False)
        nombre_equipo = equipo["nombre"] if equipo else "Desconocido"
        estado = "Activo" if j["activo"] else "Inactivo"
        filas.append([j["id"], j["nombre"], j["posicion"], nombre_equipo, estado])
    print(filas)

def buscar_jugador():
    print("\n--- Buscar jugador ---")
    
    id_buscar = int(input("Escribe el id del jugador: "))
    if id_buscar is None:
        print("El id debe ser un numero")
        return
    jugador = utiles.buscar_jugador_por_id(id_buscar, solo_activos=False)
    if jugador is None:
        print("No existe ese jugador")
        return
    equipo = utiles.buscar_equipo_por_id(jugador["equipo_id"], solo_activos=False)
    nombre_equipo = equipo["nombre"] if equipo else "Desconocido"
    estado = "Activo" if jugador["activo"] else "Inactivo"
    
    print(f"\nID: {jugador['id']}")
    print(f"Nombre: {jugador['nombre']}")
    print(f"Posicion: {jugador['posicion']}")
    print(f"Equipo: {nombre_equipo}")
    print(f"Estado: {estado}")

def actualizar_jugador():
    print("\n--- Actualizar jugador ---")
    
    id_jugador = int(input("Escribe el id del jugador que quieres actualizar: "))
    if id_jugador is None:
        print("El id debe ser un numero")
        return
    jugador = utiles.buscar_jugador_por_id(id_jugador, solo_activos=True)
    if jugador is None:
        print("Ese jugador no existe o no esta activo")
        return
    nuevo_nombre = str(input("Escribe el nuevo nombre del jugador: "))
    nueva_posicion = str(input("Escribe la nueva posicion del jugador: "))
    entrada_equipo = input("Escribe el nuevo id del equipo ")
    if nuevo_nombre and len(nuevo_nombre) > 0:
        jugador["nombre"] = nuevo_nombre
    if nueva_posicion and len(nueva_posicion) > 0:
        jugador["posicion"] = nueva_posicion
    if entrada_equipo and entrada_equipo.isdigit():
        nuevo_equipo_id = int(entrada_equipo)
        equipo = utiles.buscar_equipo_por_id(nuevo_equipo_id, solo_activos=True)
        if equipo:
            jugador["equipo_id"] = nuevo_equipo_id
        else:
            print("Ese equipo no existe o no esta activo")
    
    print("Hemos actualizado a tu jugador")

def eliminar_jugador():
    print("\n--- Eliminar o reactivar jugador ---")
    
    id_eliminar = int(input("Escribe el id del jugador: "))
    if id_eliminar is None:
        print("El id debe ser un numero")
        return
    jugador = utiles.buscar_jugador_por_id(id_eliminar, solo_activos=False)
    if jugador is None:
        print("Ese jugador no existe")
        return
    if jugador["activo"]:
        str(input("Si quieres eliminar a ese jugador escribe s :")).lower
        jugador["activo"] = False
        print("Hemos eliminado a ese jugador")
    else:
        str(input("Si quieres activar a ese jugador escribe s :")).lower
        jugador["activo"] = True
        print("Hemos activado a ese jugador")

def menu_jugadores():
    salir = False
    while not salir:
        print("--- Menu de jugadores ---")
        print("1. Crear jugador")
        print("2. Listar jugadores")
        print("3. Buscar jugador por id")
        print("4. Actualizar jugador")
        print("5. Eliminar o reactivar jugador")
        print("6. Volver")
        opcion = input("Elige una de las opciones: ")
        
        if opcion == "1":
            crear_jugador()
        elif opcion == "2":
            listar_jugadores()
        elif opcion == "3":
            buscar_jugador()
        elif opcion == "4":
            actualizar_jugador()
        elif opcion == "5":
            eliminar_jugador()
        elif opcion == "6":
            salir = True
        else:
            print("Esa opcion no existe")
