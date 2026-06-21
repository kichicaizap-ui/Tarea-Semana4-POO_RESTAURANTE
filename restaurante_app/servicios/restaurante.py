# Clase que administra productos y clientes

class Restaurante:

    # Constructor de la clase Restaurante
    def __init__(self):
        self.productos = []  # Lista para guardar productos
        self.clientes = []   # Lista para guardar clientes

    # Agrega un producto a la lista
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Agrega un cliente a la lista
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Muestra todos los productos registrados
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    # Muestra todos los clientes registrados
    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)