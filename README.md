[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre: Miguel Angel londono Rubiano  
ID:  000421385
---
# Organización de clientes Y almuerzos en un restaurante.

## Problema a solucionar:
Para un restaurante es de vital importancia mantener una correcta organización en los clientes, pedidos, platos y costos en cada orden, por esto se realizará un programa en el cual se puedan ordenar todos estos datos bajo una estructura sencilla, que le permita al usuario/trabajador facilitar su labor y que para él sea más sencillo saber que a que mesa le pertenece cada orden, que alimentos contiene cada orden y el costo total del servicio, visualizando todo esto en el programa. 
# Utilidad del programa:
Una de las principales necesidades en un restaurante es el orden y que este mismo sea eficiente, el brindarle una herramienta al mesero que le permita visualizar las mesas del restaurante, poder asignar las ordenes y conocer la cuenta de cada una de ellas, le ahorrará tiempo y le permitirá ser más eficiente a la hora de entregar los pedidos.
Lo que se termina traduciendo en un mejor servicio, porque un servicio más rápido es una mejor atención, vital a la hora de atender a las personas, el ser más organizado permitirá también evitar errores en contabilidad y con los clientes. 
El saber cuántos platos se vendieron, y los ingresos diarios ayudara a tomar decisiones en la administración. 

# Alcance
## Funcionalidades:
El programa le permitirá visualizar al trabajador las mesas del restaurante, escoger una mesa de las enumeradas disponibles (mostrara cuales están ocupadas y desocupadas), a estas se le podrán asignar las diferentes opciones de almuerzo que se tengan en ese día. Para al final sumar los costos en cada mesa y dar un total en la cuenta.
También permitirá ver al final del día cuantos platos se pidieron de cada cosa. 
## Que situaciones cubre:
Cubre una situación cotidiana, en la que los menús y las mesas ya están definidas, en caso de que en el restaurante junten varias mesas y/o venda un plato que no está definido, la opción no estará contemplada, y se tendrá que seleccionar alguna de las mesas que se usó para juntar, y/o añadir el plato que no esta definido.
(No hay opción mesa personalizada ni plato personalizado)

# Estructuras de Datos Utilizadas:
para realizar el programa se utilizaron distintas metodologias y estructuras vistas en clase ,emplenado lo que es una lista de listas (en la parte de las mesas) para representar las mesas del restaurante,que como tal desee que fueran cinco mesas, donde cada elemento indica si una mesa está disponible (0) u ocupada (1). tambien, se usaron diccionarios para guardar el menú de platos y bebidas junto con sus precios. El diccionario de pedidos funciona asociando cada mesa con una lista que contiene los platos y bebidas ordenados por la mesa seleccionada .Esto nos permite llevar un registro de los artículos seleccionados y calcular el total de la cuenta de cada mesa.
