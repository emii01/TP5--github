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

menu()
