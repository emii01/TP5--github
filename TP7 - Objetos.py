"""ejercicio 1"""
# class rectangulo():
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def calcularArea(self):
#         area = self.base * self.altura
#         print(f"El area del rectangulo es {area}")

# rectangulo1 = rectangulo(5, 5)
# rectangulo1.calcularArea()

"""ejercicio 2"""
# class mate():
#     def __init__(self, n):
#         self.cebadasRestantes = n
#         self.estado = False
#         self.n = n

#     def cebarMate(self):
#         if self.estado == True:
#             print("¡Cuidado! ¡Te quemaste!")
#         else:
#             self.estado = True
#             self.cebadasRestantes -= 1
#             print("Cebaste el mate")

#     def beberMate(self):
#         if self.estado == False:
#             print("El mate esta vacio!")
#         else:
#             self.estado = False
#             self.cebadasRestantes -= 1
#             print("Bebiste el mate")

#         if self.cebadasRestantes < 0:
#             self.cebadasRestantes -= 1
#             print("Advertencia. El mate esta lavado")

# mateUno = mate(3)
# mateUno.cebarMate()
# mateUno.beberMate()
# mateUno.cebarMate()
# mateUno.beberMate()
# mateUno.beberMate()
# mateUno.cebarMate()
# mateUno.cebarMate()
# mateUno.beberMate()
# mateUno.cebarMate()
# mateUno.beberMate()

"""ejercicio 3"""
# class corcho():
#     def __init__(self, bodega):


# class botella():
#     def __init__(self, corcho = None):
#         self.corcho = corcho

#     def esta_destapada(self):
#         self.corcho = None

# class sacachorchos():
#     def __init__(self):
#         self.corcho = None

#     def destapar(self, botella):
#         if self.corcho is not None:
#             print("El sacacorcho ya contiene un corcho")

#         if botella.esta_destapada():
#             print("La botella ya esta destapada")

#         self.corcho = botella.corcho
#         botella.corcho = None
      
#     def limpiar(self):
#         if self.corcho is None:
#             print("El sacacorchos no tiene ningun corcho para limpiar")
#         else:
#             self.corcho = None
#             print("Limpiaste el sacacorcho")

# corchoo = corcho("BodegaUno")

"""ejercicio 4"""
# class Restaurante:
#     def __init__(self, nombre, tipo_comida):
#         self.nombre = nombre
#         self.tipo_comida = tipo_comida

#     def describir_restaurante(self):
#         print(f"Restaurante: {self.nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")

#     def abrir_restaurante(self):
#         print(f"El restaurante {self.nombre} está abierto.")


# class Heladeria(Restaurante):
#     def __init__(self, nombre, tipo_comida, sabores):
#         Restaurante.__init__(self, nombre, tipo_comida)
#         self.sabores = sabores

#     def mostrar_sabores(self):
#         print("Sabores disponibles:")
#         for sabor in self.sabores:  
#             print(f" {sabor}")


# mi_heladeria = Heladeria("Grido", "Postres", ["Chocolate", "Fresa", "Vainilla"])

# mi_heladeria.describir_restaurante()
# mi_heladeria.abrir_restaurante()
# mi_heladeria.mostrar_sabores()

"""ejercicio 5"""
#no lo entendi

"""ejercicio 6"""
# class Usuario:
#     def __init__(self, nombre, apellido, edad, email):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.email = email

#     def describir_usuario(self):
#         print(f"Nombre: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Correo: {self.email}")

#     def saludar_usuario(self):
#         print(f"¡Hola, {self.nombre}, como estas?")

"""ejercicio 7"""
# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, email, privilegios):
#         Usuario.__init__(self, nombre, apellido, edad, email)
#         self.privilegios = privilegios

#     def mostrar_privilegios(self):
#         print("Privilegios del administrador:")
#         for privilegio in self.privilegios:
#             print(f" {privilegio}")


# admin1 = Admin(
#     "Martina", 
#     "López", 
#     35, 
#     "martina@gmail.com", 
#     ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]
# )

# admin1.describir_usuario()
# admin1.saludar_usuario()
# admin1.mostrar_privilegios()


# usuario1 = Usuario("Juan", "Pérez", 30, "juan.perez@gmail.com")
# usuario2 = Usuario("Ana", "Gómez", 25, "ana.gomez@gmail.com")
# usuario3 = Usuario("Carlos", "Ramírez", 40, "carlos@gmail.com")

# print("Usuario 1:")
# usuario1.describir_usuario()
# usuario1.saludar_usuario()

# print("Usuario 2:")
# usuario2.describir_usuario()
# usuario2.saludar_usuario()

# print("Usuario 3:")
# usuario3.describir_usuario()
# usuario3.saludar_usuario()


