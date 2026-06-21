# Importar las clases desde sus respectivos archivos
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear un objeto de tipo Restaurante
restaurante = Restaurante()

# Crear productos
p1 = Producto("Pizza", 8.50)
p2 = Producto("Jugo Natural", 2.00)

# Crear clientes
c1 = Cliente("Juan Perez", "1101234567")
c2 = Cliente("Maria Lopez", "1109876543")

# Agregar productos al restaurante
restaurante.agregar_producto(p1)
restaurante.agregar_producto(p2)

# Agregar clientes al restaurante
restaurante.agregar_cliente(c1)
restaurante.agregar_cliente(c2)

# Mostrar los productos registrados
print("=== PRODUCTOS ===")
restaurante.mostrar_productos()

# Mostrar los clientes registrados
print("\n=== CLIENTES ===")
restaurante.mostrar_clientes()