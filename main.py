"""
- registrar alumnos
- generar fichas de matriculas
- mostrar la lista de todos los matriculados
- filtrar matriculados por programa de estudio
"""
lista_alumnos=[]
#inicio del problema
#nesecito poder agregar mas alumnos sin la nesecidad de crear tantas variables
#posible solucion cre o o enceñar el codigo en un ciclo while
nombre=input("ingrese el nombre del alumno: ")
apellido=input("ingrese el apellido del alumno: ")
nombre2=input("ingrese el nombre del alumno: ")
apellido2=input("ingrese el apellido del alumno: ")
lista_alumnos.append(nombre)
lista_alumnos.append(apellido)

alumno={
    "nombre":nombre,
    "apellido":apellido
}
alumno2={
    "nombre":nombre2,
    "apellido":apellido2
}
lista_alumnos.append(nombre2)
lista_alumnos.append(apellido2)
#fin del problema

#deseo mostrar un meno con las opciones de agregar un nuevo alumno y salir del programa. 
print (lista_alumnos)
