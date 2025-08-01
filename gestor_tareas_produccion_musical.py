from funciones_musica import agregar_cancion, agregar_tarea, ver_tareas, marcar_tarea_completada, editar_tarea

canciones = {}

while True:
    print("\n🎹 MENÚ PRINCIPAL")
    print("1. Agregar canción")
    print("2. Agregar tarea a canción")
    print("3. Ver checklist de una canción")
    print("4. Marcar tarea como completada")
    print("5. Editar tarea")
    print("6. Ver canciones existentes")
    print("7. Salir")




    eleccion = input("Selecciona una opción (1-7): ")

    if eleccion == "1":
        agregar_cancion(canciones)

    elif eleccion == "2":
        agregar_tarea(canciones)

    elif eleccion == "3":
        ver_tareas(canciones)

    elif eleccion == "4":
        marcar_tarea_completada(canciones)

    elif eleccion == "5":
        editar_tarea(canciones)

    elif eleccion == "6":
        if not canciones:
            print("❌ No hay canciones aún.")
        else:
            print("\n🎼 Canciones actuales:")
            for nombre, datos in canciones.items():
                print(f"- {nombre} (Artista: {datos['artista']})")

    elif eleccion == "7":
        print("Nos vemos pronto! 👋")
        break
