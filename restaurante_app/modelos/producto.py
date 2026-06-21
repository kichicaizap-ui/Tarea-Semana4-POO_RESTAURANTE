# Clase que representa un producto del restaurante

class Producto:

    # Constructor: se ejecuta cuando se crea un producto
    def __init__(self, nombre, precio):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto

    # Permite mostrar el objeto como texto
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"