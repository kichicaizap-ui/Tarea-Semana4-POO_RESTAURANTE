# Sistema de Gestión de Restaurante

## Nombre del estudiante

Iveth Chicaiza

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema básico de gestión de restaurante utilizando Programación Orientada a Objetos (POO) en Python.

El objetivo principal es representar algunos elementos de un restaurante mediante clases y objetos, aplicando conceptos como constructores, atributos, métodos, importaciones y organización modular del código.

El sistema permite registrar productos disponibles en el restaurante y clientes registrados, además de mostrar la información almacenada de forma organizada en la consola.

## Estructura del proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py

README.md
```

## Explicación de los archivos

### producto.py

Contiene la clase Producto, encargada de representar los productos que ofrece el restaurante, como platos o bebidas. Cada producto posee atributos como nombre y precio.

### cliente.py

Contiene la clase Cliente, que representa a las personas registradas en el sistema. Cada cliente cuenta con información básica como nombre y número de cédula.

### restaurante.py

Contiene la clase Restaurante, responsable de administrar los productos y clientes registrados. Además, incluye métodos para agregar y mostrar información.

### main.py

Es el archivo principal del programa. Aquí se crean los objetos, se registran los productos y clientes, y se ejecutan los métodos necesarios para demostrar el funcionamiento del sistema.

## Funcionalidades implementadas

* Creación de clases utilizando Programación Orientada a Objetos.
* Uso de constructores mediante el método **init**().
* Definición de atributos y métodos.
* Implementación del método especial **str**() para representar objetos como texto.
* Organización del proyecto en módulos.
* Uso de importaciones entre archivos.
* Registro y visualización de productos y clientes.

## Reflexión

La realización de este proyecto me permitió comprender mejor la importancia de la Programación Orientada a Objetos y la organización modular del software. Separar las clases en diferentes archivos facilita el mantenimiento del código, mejora la legibilidad y permite reutilizar componentes de forma más eficiente. Además, esta estructura ayuda a desarrollar programas más ordenados y fáciles de ampliar en el futuro.
