# Clase que representa a un cliente

class Cliente:

    # Constructor de la clase Cliente
    def __init__(self, nombre, cedula):
        self.nombre = nombre  # Nombre del cliente
        self.cedula = cedula  # Número de cédula del cliente

    # Devuelve la información del cliente en formato texto
    def __str__(self):
        return f"{self.nombre} - {self.cedula}"