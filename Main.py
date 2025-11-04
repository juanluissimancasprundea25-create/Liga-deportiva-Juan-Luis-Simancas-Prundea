import equipos
import jugadores
import calendario
import ranking

def menu_principal():
    salir = False
    while not salir:
        print("--- Menu principal ---")
        print("1. Gestion de equipos")
        print("2. Gestion de jugadores")
        print("3. Calendario de partidos")
        print("4. Resultados y clasificación")
        print("5. Salir")
        opcion = input("Elige una de las opciones: ")
        
        if opcion == "1":
            equipos.menu_equipos()
        elif opcion == "2":
            jugadores.menu_jugadores()
        elif opcion == "3":
            calendario.menu_partidos()
        elif opcion == "4":
            ranking.menu_resultados()
        elif opcion == "5":
            salir = True
            print("\nAdios")
        else:
            print("Esa opción no existe")

if __name__ == "__main__":
    menu_principal()
