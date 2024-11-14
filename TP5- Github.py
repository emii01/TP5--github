# """ejercicio 1"""
# escuela = {
#     "alumnos" : []
# }

# def agregarAlumno(nombre, apellido, fechaNacimiento, dni, nombreTutor):
#     alumno = {
#         "nombre": nombre,
#         "apellido": apellido,
#         "fechaDeNacimiento": fechaNacimiento,
#         "DNI": dni,
#         "nombreTutor": nombreTutor,
#         "notas": [],
#         "cantidadFaltas": 0,
#         "cantidadAmonestaciones": 0
#     }

# def agregarNota(dni ,nota):
#     for alumno in escuela["alumnos"]:
#         if alumno["DNI"] == dni:
#             alumno["notas"].append(nota)
#             print(f"nota {nota} agregada para el alumno {alumno["nombre"]} {alumno["apellido"]}")
#         else:
#             print("alumno NO encontrado")

# def agregarFaltas(dni):
#     for alumno in escuela["alumnos"]:
#         if alumno["DNI"] == dni:
#             alumno["cantidadFaltas"] += 1
#             print(f"se registro la falta para el alumno {alumno["nombre"]} {alumno["apellido"]}")
#         else:
#             print("Alumno NO encontrado")

# def agregarAmonestaciones(dni):
#     for alumno in escuela["alumnos"]:
#         if alumno["DNI"] == dni:
#             alumno["cantidadAmonestaciones"] += 1
#             print(f"Se registro una amonestacion para el alumno {alumno["nombre"]} {alumno["apellido"]}")

# def eliminarAlumnos(dni):
#     for i, alumno in escuela["alumnos"]:
#         if alumno["DNI"] == dni:
#             eliminado = escuela["alumnos"].pop(i)
#             print(f"Alumno {eliminado["nombre"]} {eliminado["apellido"]} expulsado del colegio")

# def mostrarAlumnos(dni):
#     for alumno in escuela["alumnos"]:
#         if alumno["DNI"] == dni:
#             print("INFORMACION DEL ALUMNO")
#             print(f"Nombre: {alumno["nombre"]}")
#             print(f"Apellido: {alumno["apellido"]}")
#             print(f"Fecha de nacimiento: {alumno["fechaDeNacimiento"]}")
#             print(f"DNI: {alumno["DNI"]}")
#             print(f"Nombre del Tutor: {alumno["nombreTutor"]}")
#             print(f"Notas: {alumno["notas"]}")
#             print(f"Cantidad de Faltas: {alumno["cantidadFaltas"]}")
#             print(f"Cantidad de Amonestaciones: {alumno["cantidadAmonestaciones"]}")
#         else:
#             print("Alumno NO encontrado")

# agregarAlumno = ("emiliano", "buhajeruk", "26-01-06", "46666920", "Fabiana")
# agregarAlumno = ("sofia", "llanos", "22-06-09", "39001242", "Carre")
# agregarNota = ("46666920", 8.5)
# agregarNota = ("46666920", 9.0)

# Sistema de gestión de alumnos


escuela = {
    "Alumnos": []
}

def mostrar_datos_alumnos():
    if not escuela["Alumnos"]:
        print("No hay alumnos registrados.")
    else:
        for alumno in escuela["Alumnos"]:
            print(" Datos del alumno ")
            for key, value in alumno.items():
                print(f"{key}: {value}")

def agregar_alumno():
    nombre = input("Nombre del alumno: ")
    apellido = input("Apellido del alumno: ")
    dni = input("DNI del alumno: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ")
    tutor = input("Nombre y apellido del tutor: ")
    notas = list(map(float, input("Notas del alumno ").split(",")))
    faltas = int(input("Cantidad de faltas: "))
    amonestaciones = int(input("Cantidad de amonestaciones: "))

    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }
    
    escuela["Alumnos"].append(nuevo_alumno)
    print("Alumno agregado exitosamente")

def modificar_datos_alumno():
    dni = input("Ingrese el DNI del alumno que desea modificar: ")
    for alumno in escuela["Alumnos"]:
        if alumno["DNI"] == dni:
            print("Seleccione el dato que desea modificar:")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Fecha de nacimiento")
            print("4. Tutor")
            print("5. Notas")
            print("6. Faltas")
            print("7. Amonestaciones")
            
            opcion = int(input("Opción: "))
            
            if opcion == 1:
                alumno["Nombre"] = input("Nuevo nombre: ")
            elif opcion == 2:
                alumno["Apellido"] = input("Nuevo apellido: ")
            elif opcion == 3:
                alumno["Fecha de nacimiento"] = input("Nueva fecha de nacimiento (DD/MM/AAAA): ")
            elif opcion == 4:
                alumno["Tutor"] = input("Nuevo nombre y apellido del tutor: ")
            elif opcion == 5:
                alumno["Notas"] = list(map(float, input("Nuevas notas ").split(",")))
            elif opcion == 6:
                alumno["Faltas"] = int(input("Nueva cantidad de faltas: "))
            elif opcion == 7:
                alumno["Amonestaciones"] = int(input("Nueva cantidad de amonestaciones: "))
            else:
                print("Opción no válida.")
            print("Datos actualizados con éxito")
            return
    print("Alumno no encontrado.")

def expulsar_alumno():
    dni = input("Ingrese el DNI del alumno a expulsar: ")
    for alumno in escuela["Alumnos"]:
        if alumno["DNI"] == dni:
            escuela["Alumnos"].remove(alumno)
            print("Alumno expulsado exitosamente")
            return
    print("Alumno no encontrado.")

# def calcular_promedio(alumno):
#     if alumno["Notas"]:
#          promedio = sum(alumno["Notas"] / len(alumno["Notas"]))
#          return promedio
#     else:
#          return 0


def menu():
    while True:
        print(" MENU DE GESTION ESCOLAR ")
        print("1. Mostrar datos de los alumnos")
        print("2. Agregar alumno")
        print("3. Modificar datos de un alumno")
        print("4. Expulsar alumno")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            mostrar_datos_alumnos()
        elif opcion == 2:
            agregar_alumno()
        elif opcion == 3:
            modificar_datos_alumno()
        elif opcion == 4:
            expulsar_alumno()
        elif opcion == 5:
            print("Saliendo del programa escolar")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
