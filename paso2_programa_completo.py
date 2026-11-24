# ============================================================
# SISTEMA DE GESTIÓN DE ESTUDIANTES — Versión final (Paso 2)
# ------------------------------------------------------------
# Funcionalidades implementadas:
#   1. Registrar nuevo estudiante (con validación de datos)
#   2. Ver lista completa de estudiantes registrados
#   3. Buscar estudiante por nombre
#   4. Salir del sistema (guardando los datos)
#
# Estructuras lógicas aplicadas:
#   - Condicionales : if / elif / else
#   - Bucles         : while (menú principal y validación)
#                      for  (recorrido de listas)
#   - Funciones      : cada tarea del programa en una función
#   - Comentarios    : explican las partes importantes del código
# ============================================================

import json
import os

# Nombre del archivo donde se guardan los datos entre ejecuciones.
ARCHIVO_DATOS = "estudiantes.json"

# Lista principal de estudiantes.
# Cada estudiante es un diccionario con 3 claves:
# {"nombre": "Ana Pérez", "edad": 20, "carrera": "Sistemas"}
estudiantes = []


# ------------------------------------------------------------
# Carga y guardado de los datos
# ------------------------------------------------------------
def cargar_datos():
    """Carga los estudiantes guardados en el archivo JSON, si existe."""
    global estudiantes
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            estudiantes = json.load(archivo)


def guardar_datos():
    """Guarda la lista actual de estudiantes en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)


# ------------------------------------------------------------
# Opción 1: Registrar estudiante
# ------------------------------------------------------------
def registrar_estudiante():
    """Solicita los datos de un estudiante, los valida y los guarda."""
    print("\n--- REGISTRAR NUEVO ESTUDIANTE ---")

    # Nombre: no puede quedar vacío
    nombre = input("Ingrese el nombre completo: ").strip()
    if nombre == "":
        print("❌ El nombre no puede estar vacío.")
        return

    # Edad: bucle while que repide la pregunta hasta que sea válida
    while True:
        edad_texto = input("Ingrese la edad: ").strip()
        if edad_texto.isdigit() and 5 <= int(edad_texto) <= 120:
            edad = int(edad_texto)
            break
        print("❌ Edad inválida. Ingrese un número entero entre 5 y 120.")

    # Carrera o curso: tampoco puede quedar vacía
    carrera = input("Ingrese la carrera o curso: ").strip()
    if carrera == "":
        print("❌ La carrera no puede estar vacía.")
        return

    # Condicional: evita registrar dos veces el mismo nombre
    for est in estudiantes:
        if est["nombre"].lower() == nombre.lower():
            print(f"⚠️ Ya existe un estudiante registrado como '{nombre}'.")
            return

    # Se crea el registro como diccionario y se agrega a la lista
    estudiante = {"nombre": nombre, "edad": edad, "carrera": carrera}
    estudiantes.append(estudiante)
    guardar_datos()
    print(f"✅ Estudiante '{nombre}' registrado exitosamente.")


# ------------------------------------------------------------
# Opción 2: Ver lista de estudiantes
# ------------------------------------------------------------
def ver_lista():
    """Muestra todos los estudiantes registrados en forma de lista."""
    print("\n--- LISTA DE ESTUDIANTES REGISTRADOS ---")

    # Condicional: aviso si la lista está vacía
    if len(estudiantes) == 0:
        print("⚠️ No hay estudiantes registrados todavía.")
        return

    # Bucle for: recorre la lista completa mostrando cada registro
    for indice, est in enumerate(estudiantes, start=1):
        print(f"\nEstudiante #{indice}")
        print(f"  Nombre:  {est['nombre']}")
        print(f"  Edad:    {est['edad']} años")
        print(f"  Carrera: {est['carrera']}")


# ------------------------------------------------------------
# Opción 3: Buscar estudiante por nombre
# ------------------------------------------------------------
def buscar_estudiante():
    """Busca estudiantes cuyo nombre contenga el texto ingresado."""
    print("\n--- BUSCAR ESTUDIANTE ---")
    criterio = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()

    encontrados = []
    # Bucle for: compara el texto ingresado con cada nombre registrado
    for est in estudiantes:
        if criterio in est["nombre"].lower():
            encontrados.append(est)

    # Condicionales según el resultado de la búsqueda
    if len(encontrados) == 0:
        print("❌ No se encontró ningún estudiante con ese nombre.")
    else:
        print(f"✅ Se encontraron {len(encontrados)} resultado(s):")
        for est in encontrados:
            print(f"  - {est['nombre']} | {est['edad']} años | {est['carrera']}")


# ------------------------------------------------------------
# Menú principal
# ------------------------------------------------------------
def mostrar_menu():
    """Imprime el menú de opciones del sistema."""
    print("\n" + "=" * 45)
    print("       SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("=" * 45)
    print("  1. Registrar nuevo estudiante")
    print("  2. Ver lista completa de estudiantes")
    print("  3. Buscar estudiante por nombre")
    print("  4. Salir del sistema")
    print("=" * 45)


def main():
    """Función principal: carga los datos y ejecuta el menú en bucle."""
    cargar_datos()
    print("🎉 ¡Bienvenido/a al Sistema de Gestión de Estudiantes!")

    # Bucle while: el menú se repite hasta elegir la opción 4 (salir)
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        # Estructura condicional que ejecuta la función correspondiente
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            ver_lista()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            guardar_datos()
            print("\n👋 Datos guardados correctamente. ¡Hasta pronto!")
            break  # Sale del bucle y termina el programa
        else:
            print("❌ Opción no válida. Elija una opción del 1 al 4.")


# Punto de entrada del programa: se ejecuta main() solo al correr este archivo
if __name__ == "__main__":
    main()
