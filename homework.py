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
# CORRECION
lista_alumnos=[] 
def mensaje_menu(): 
  menu_opciones="""
   --------Bienvenido al Sistema--------
   ----------Regitra tu alumno----------
   1. Escribe (s) si deseas agregar un nuevo alumno
   2. Escribe (n) si deseas salir del sistema 
   Escribe la Accion que desea realiza:"""
   return menu_opciones=""
def ingresar_datos_alumno():  
  id=len(lista_alumnos)+1 
  cui=int(input("Ingrese el numero de su dni: ")) 
  nombre=input("Ingrese el nombre del alumno: ") 
  apellido input("Ingrese el apeliido del alumno: ") 
  numero_celular=int(input("Ingrese su numero de celular: ")) 
  programa_estudio=input("Ingrese el programa de estudio: ") 
  ciclo_academico=input("Ingrese su ciclo academico: ") 
  email=input("Ingrese su correo electronico: ") 
  guardar_datos_alumno(id, cui, nombre, apellido, numero_celular, programa_estudio, ciclo_academico, email)
def guardar_datos_alumno(id, cui, nombre, apellido, numero_celular, programa_estudio, ciclo_academico,email): 
  alumno={ 
    "id":id, 
    "cui":cui, 
    "nombre": nombre, 
    "apellido": apellido,
    "numero_celular": numero_celular, 
    "programa_estudio": programa_estudio, 
    "ciclo_academico":ciclo_academico, 
    "email":email 
    ´}
  lista_alumnos.append(alumno)

while True: 
    menu_opciones input(mensaje_sonu())
    if menu opciones.lower() --"n": 
      print("Saliendo del Sistema") 
      break 
    elif menu opciones.lower() --"s" 
         Ingresar datos_alumno() 
    else:
       print("Opcion erronea") 
print(lista_alumnos)
## modularizar