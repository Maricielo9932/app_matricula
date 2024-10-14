lista_alumnos = []

def registrar_alumno():
    """Registra un nuevo alumno y lo agrega a la lista."""
    nombre = input("Ingrese el nombre del alumno: ")
    programa = input("Ingrese el programa de estudio: ")
    alumno = {"nombre": nombre, "programa": programa}
    lista_alumnos.append(alumno)
    print("Alumno registrado correctamente.")

def generar_ficha_matricula(alumno):
    """Genera la ficha de matrícula de un alumno."""
    print("-" * 20)
    print(f"Nombre: {alumno['nombre']}")
    print(f"Programa: {alumno['programa']}")
    print("-" * 20)

def mostrar_lista_matriculados():
    """Muestra la lista de todos los alumnos matriculados."""
    if not lista_alumnos:
        print("No hay alumnos matriculados.")
        return
    for alumno in lista_alumnos:
        generar_ficha_matricula(alumno)

while True:
    print("\nMenú:")
    print("1. Registrar alumno")
    print("2. Mostrar lista de matriculados")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_alumno()
    elif opcion == "2":
        mostrar_lista_matriculados()
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")
















