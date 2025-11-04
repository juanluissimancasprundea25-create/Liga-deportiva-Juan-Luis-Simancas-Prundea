import utiles

def crear_equipo():
    print("\n--- Crear equipo ---")
    
    nombre = str(input("Escribe el nombre del equipo: "))
    if nombre is None:
        print("El nombre no puede estar vacio")
        return
    ciudad = str(input("Escribe la ciudad del equipo: "))
    if ciudad is None:
        print("La ciudad no puede estar vacia")
        return
    equipo = {"id": utiles.generar_id("equipo"), "nombre": nombre, "ciudad": ciudad, "activo": True}
    utiles.equipos.append(equipo)
    print(f"Hemos creado el equipo '{nombre}' con id {equipo['id']}")

def listar_equipos():
    print("\n--- Lista de equipos activos ---")
    
    equipos_activos = [e for e in utiles.equipos if e["activo"]]
    if not equipos_activos:
        print("No hay equipos activos")
        return
    filas = [[e["id"], e["nombre"], e["ciudad"], "Activo"] for e in equipos_activos]
    print(filas)

def buscar_equipo():
    print("\n--- Buscar equipo ---")
    
    id_buscar = int(input("Escribe el id del equipo: "))
    if id_buscar is None:
        print("El id no puede estar vacio")
        return
    equipo = utiles.buscar_equipo_por_id(id_buscar, solo_activos=False)
    if equipo is None:
        print("Ese equipo no existe")
        return
    estado = "Activo" if equipo["activo"] else "Inactivo"
    print(f"\nID: {equipo['id']}")
    print(f"Nombre: {equipo['nombre']}")
    print(f"Ciudad: {equipo['ciudad']}")
    print(f"Estado: {estado}")

def actualizar_equipo():
    print("\n--- Actualizar equipo ---")
    
    id_editar = int(input("Escribe el id del equipo que quieres actualizar: "))
    if id_editar is None:
        print("El id no puede estar vacio")
        return
    equipo = utiles.buscar_equipo_por_id(id_editar, solo_activos=True)
    if equipo is None:
        print("El equipo no existe o esta inactivo")
        return
    nuevo_nombre = input("Escribe el nuevo nombre del equipo: ")
    nueva_ciudad = input("Escribe el nuevo nombre de la ciudad: ")
    if nuevo_nombre and len(nuevo_nombre) > 0:
        equipo["nombre"] = nuevo_nombre
    if nueva_ciudad and len(nueva_ciudad) > 0:
        equipo["ciudad"] = nueva_ciudad
    print("Hemos actualizado tu equipo")

def eliminar_equipo():
    print("\n--- Eliminar o activar equipo ---")
    
    id_eliminar = int(input("Escribe el id del equipo: "))
    if id_eliminar is None:
        print("El id no puede estra vacio")
        return
    equipo = utiles.buscar_equipo_por_id(id_eliminar, solo_activos=False)
    if equipo is None:
        print("Ese equipo no existe")
        return
    if equipo["activo"]:
        str(input("Si quieres desactivar este equipo escribe s :")).lower
        equipo["activo"] = False
        print("Hemos deactivado ese equipo")
    else:
        str(input("Si quieres activa este equipo escribe s :")).lower
        equipo["activo"] = True
        print("Hemos activado ese equipo")

def menu_equipos():
    salir = False
    while not salir:
        print("--- Menu de equipos ---")
        print("1. Crear equipo")
        print("2. Listar equipos")
        print("3. Buscar equipo por id")
        print("4. Actualizar equipo")
        print("5. Eliminar o activar equipo")
        print("6. Volver")
        opcion = input("Elige una de las opciones: ")
        
        if opcion == "1":
            crear_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            buscar_equipo()
        elif opcion == "4":
            actualizar_equipo()
        elif opcion == "5":
            eliminar_equipo()
        elif opcion == "6":
            salir = True
        else:
            print("Esa opcion no existe")
