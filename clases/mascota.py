class Mascota:
    def __init__(self, nombre, edad, salud, precio):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio

    def actualizar_informacion(self, edad=None, salud=None, precio=None):
        if edad is not None:
            self.edad = edad
        if salud is not None:
            self.salud = salud
        if precio is not None:
            self.precio = precio

    def mostrar_informacion(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}"


class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, nivel_de_energia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.nivel_de_energia = nivel_de_energia  # Sin tilde

    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Nivel de Energía: {self.nivel_de_energia}"


class Gato(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.independencia = independencia

    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Independencia: {self.independencia}"
