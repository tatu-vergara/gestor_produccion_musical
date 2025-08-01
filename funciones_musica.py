TAREAS_POR_DEFECTO = {
    "Pre-producción": [
        "Escribir letra",
        "Componer estructura"
    ],
    "Producción": [
        "Grabar voces",
        "Grabar instrumentos",
        "Editar (alinear, afinar)",
        "Elegir sonidos/samples",
        "Arreglos"
    ],
    "Mezcla": [
        "Agregar efectos",
        "Ecualizar",
        "Comprimir",
        "Distribuir dinámicas"
    ],
    "Máster": [
        "Exportar Stems",
        "Enviar mezcla en 48khz - 24 bits"
    ]
}

def agregar_cancion(diccionario_canciones):
    nombre = input("Ingrese el nombre de la canción: ")

    if nombre in diccionario_canciones:
        print("❌ Ya existe una canción con ese nombre. Prueba con otro nombre.")
        return

    artista = input("Ingrese el nombre del artista: ")

    cancion = {
        "nombre": nombre,
        "artista": artista,
        "tarea": {
            "Pre-producción": [],
            "Producción": [],
            "Mezcla": [],
            "Máster": []
        }
    }

    diccionario_canciones[nombre] = cancion
    print(f"\n✅ Canción '{nombre}' del artista '{artista}' fue agregada correctamente.\n")



def agregar_tarea(diccionario_canciones):
    if not diccionario_canciones:
        print("❌ No hay canciones registradas. Agrega una canción primero.")
        return

    print("\n🎵 Canciones disponibles:")
    for nombre in diccionario_canciones:
        print(f"- {nombre}")

    seleccion = input("Escribe el nombre de la canción a la que quieres agregarle una tarea: ")

    if seleccion not in diccionario_canciones:
        print("❌ Esa canción no existe. Intenta de nuevo.")
        return

    cancion = diccionario_canciones[seleccion]
    print(f"\n🎯 Trabajando en '{seleccion}' del artista '{cancion['artista']}'\n")

    print("Selecciona una categoría para agregar la tarea:")
    print("1. Pre-producción")
    print("2. Producción")
    print("3. Mezcla")
    print("4. Máster")
    print("5. Agregar tareas por defecto")
    print("6. Cancelar")

    opcion = input("Elige una opción (1-6): ")

    categorias = {
        "1": "Pre-producción",
        "2": "Producción",
        "3": "Mezcla",
        "4": "Máster"
    }

    if opcion == "5":
        for categoria, lista_tareas in TAREAS_POR_DEFECTO.items():
            for tarea in lista_tareas:
                nueva_tarea = {
                    "nombre": tarea,
                    "completada": False
                }
                cancion["tarea"][categoria].append(nueva_tarea)
        print("✅ Tareas por defecto agregadas exitosamente a todas las categorías.")
        return
    elif opcion == "6":
        print("🚪 Operación cancelada.")
        return
    elif opcion not in categorias:
        print("❌ Opción inválida. Intenta de nuevo.")
        return

    categoria_seleccionada = categorias[opcion]
    print(f"\n✏️ Agregando tarea a la categoría: {categoria_seleccionada}")

    nombre_tarea = input("Escribe el nombre de la tarea: ")

    nueva_tarea = {
        "nombre": nombre_tarea,
        "completada": False
    }

    cancion["tarea"][categoria_seleccionada].append(nueva_tarea)
    print(f"✅ Tarea '{nombre_tarea}' agregada a '{categoria_seleccionada}' correctamente.")



def ver_tareas(diccionario_canciones):
    if not diccionario_canciones:
        print("❌ No hay canciones registradas.")
        return

    print("\n🎵 Canciones disponibles:")
    for nombre in diccionario_canciones:
        print(f"- {nombre}")

    seleccion = input("Escribe el nombre de la canción para ver sus tareas: ")

    if seleccion not in diccionario_canciones:
        print("❌ Esa canción no existe.")
        return

    cancion = diccionario_canciones[seleccion]
    print(f"\n📝 Checklist de '{seleccion}' (Artista: {cancion['artista']})")

    tareas_por_categoria = cancion["tarea"]

    for categoria, lista_tareas in tareas_por_categoria.items():
        print(f"\n🔸 {categoria}")
        if not lista_tareas:
            print("   (Sin tareas aún)")
        else:
            for tarea in lista_tareas:
                estado = "✔" if tarea["completada"] else "✘"
                print(f"   [{estado}] {tarea['nombre']}")




def marcar_tarea_completada(diccionario_canciones):
    if not diccionario_canciones:
        print("❌ No hay canciones registradas.")
        return

    print("\n🎵 Canciones disponibles:")
    for nombre in diccionario_canciones:
        print(f"- {nombre}")

    seleccion = input("Escribe el nombre de la canción: ")

    if seleccion not in diccionario_canciones:
        print("❌ Esa canción no existe.")
        return

    cancion = diccionario_canciones[seleccion]
    tareas_por_categoria = cancion["tarea"]

    print("\n🔍 Categorías disponibles:")
    categorias_disponibles = list(tareas_por_categoria.keys())
    for i, cat in enumerate(categorias_disponibles, 1):
        print(f"{i}. {cat}")

    opcion = input("Selecciona una categoría por número: ")

    if not opcion.isdigit() or int(opcion) not in range(1, len(categorias_disponibles) + 1):
        print("❌ Opción inválida.")
        return

    categoria = categorias_disponibles[int(opcion) - 1]
    tareas = tareas_por_categoria[categoria]

    if not tareas:
        print(f"⚠️ No hay tareas en la categoría '{categoria}'.")
        return

    print(f"\n📋 Tareas en '{categoria}':")
    for i, tarea in enumerate(tareas, 1):
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{i}. [{estado}] {tarea['nombre']}")

    seleccion_tarea = input("Selecciona el número de la tarea que quieres marcar como completada: ")

    if not seleccion_tarea.isdigit() or int(seleccion_tarea) not in range(1, len(tareas) + 1):
        print("❌ Opción inválida.")
        return

    tarea_seleccionada = tareas[int(seleccion_tarea) - 1]
    if tarea_seleccionada["completada"]:
        print("ℹ️ Esa tarea ya está marcada como completada.")
    else:
        tarea_seleccionada["completada"] = True
        print(f"✅ Tarea '{tarea_seleccionada['nombre']}' marcada como completada.")



def editar_tarea(diccionario_canciones):
    if not diccionario_canciones:
        print("❌ No hay canciones registradas.")
        return

    print("\n🎵 Canciones disponibles:")
    for nombre in diccionario_canciones:
        print(f"- {nombre}")

    seleccion = input("Escribe el nombre de la canción: ")

    if seleccion not in diccionario_canciones:
        print("❌ Esa canción no existe.")
        return

    cancion = diccionario_canciones[seleccion]
    tareas_por_categoria = cancion["tarea"]

    print("\n🔍 Categorías disponibles:")
    categorias_disponibles = list(tareas_por_categoria.keys())
    for i, cat in enumerate(categorias_disponibles, 1):
        print(f"{i}. {cat}")

    opcion = input("Selecciona una categoría por número: ")

    if not opcion.isdigit() or int(opcion) not in range(1, len(categorias_disponibles) + 1):
        print("❌ Opción inválida.")
        return

    categoria = categorias_disponibles[int(opcion) - 1]
    tareas = tareas_por_categoria[categoria]

    if not tareas:
        print(f"⚠️ No hay tareas en la categoría '{categoria}'.")
        return

    print(f"\n📋 Tareas en '{categoria}':")
    for i, tarea in enumerate(tareas, 1):
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{i}. [{estado}] {tarea['nombre']}")

    seleccion_tarea = input("Selecciona el número de la tarea que quieres editar: ")

    if not seleccion_tarea.isdigit() or int(seleccion_tarea) not in range(1, len(tareas) + 1):
        print("❌ Opción inválida.")
        return

    tarea = tareas[int(seleccion_tarea) - 1]

    print("\n¿Qué deseas hacer?")
    print("1. Cambiar nombre de la tarea")
    print("2. Cambiar estado completado/no completado")
    print("3. Cancelar")

    accion = input("Elige una opción (1-3): ")

    if accion == "1":
        nuevo_nombre = input("Escribe el nuevo nombre de la tarea: ")
        anterior = tarea["nombre"]
        tarea["nombre"] = nuevo_nombre
        print(f"✏️ Tarea renombrada de '{anterior}' a '{nuevo_nombre}'.")
    elif accion == "2":
        tarea["completada"] = not tarea["completada"]
        nuevo_estado = "completada" if tarea["completada"] else "incompleta"
        print(f"🔁 Estado cambiado: ahora está marcada como {nuevo_estado}.")
    elif accion == "3":
        print("🚪 Edición cancelada.")
        return
    else:
        print("❌ Opción inválida.")
