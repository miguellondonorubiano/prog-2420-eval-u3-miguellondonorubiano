
def main():
    ## Iniciar las mesas, 0 significa disponible, 1 significa ocupada
    mesas = [[0, 0, 0, 0, 0]]

    # Lista de plaotos predefinidos por el restaurante y sus precios.
    platos = {
        1: {"nombre": "Cazuela de frijoles", "precio": 27000},
        2: {"nombre": "Bandeja Paisa", "precio": 32000},
        3: {"nombre": "Canon de cerdo", "precio": 25000},
        4: {"nombre": "Pollo a la plancha", "precio": 22000},
        5: {"nombre": "Trucha a la plancha", "precio": 27000},
        6: {"nombre": "Sancocho", "precio": 30000},
        7: {"nombre": "Ajiaco", "precio": 30000}
    }

    # lista de bebidas y sus precios.
    bebidas = {
        8: {"nombre": "Mazamorra", "precio": 4000},
        9: {"nombre": "Jarra de guandolo", "precio": 12000},
        10: {"nombre": "Jugo en agua", "precio": 8000},
        11: {"nombre": "Cerveza", "precio": 5000},
        12: {"nombre": "Tinto", "precio": 2000}
    }

    # Realizar el menú completo con las comidas y bebidas
    menu = {**platos, **bebidas}

    # para que queden almacenados los pedidos dentro de la pcion de cada mesa 
    pedidos = {1: [], 2: [], 3: [], 4: [], 5: []}

    # Función para mostrar las mesas y su estado.
    def mostrar_mesas():
        print("Estado de las mesas (🟥: Ocupada, 🟩: Disponible)")
        for i in range(5):
            estado = '🟥' if mesas[0][i] == 1 else '🟩'
            print(f"Mesa {i+1}: {estado}")
            
    # Función para asignar un plato a una mesa
    def asignar_pedido(mesa):
        print("Menú de platos:")
        for num, item in menu.items():
            print(f"{num}. {item['nombre']} - ${item['precio']}")

        while True:
            try:
                plato = int(input("Selecciona el número de referencia del plato o bebida (0 para salir): "))
                if plato == 0:
                    break
                if plato in menu:
                    pedidos[mesa].append(menu[plato])
                    mesas[0][mesa-1] = 1  # aqui marcamos si la mesa se encuentra como ocupada
                    print(f"Se ha añadido {menu[plato]['nombre']} a la mesa {mesa}.")
                else:
                    print("Plato no válido, intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Intenta nuevamente.")

    # Función para mostrar la cuenta total de la mesa
    def mostrar_cuenta(mesa):
        total = sum(item["precio"] for item in pedidos[mesa])
        print(f"Cuenta total de la mesa {mesa}: ${total}")

    # Función para mostrar la lista de los platos pedidos por la mesa
    def mostrar_pedidos(mesa):
        if len(pedidos[mesa]) == 0:
            print(f"La mesa {mesa} no tiene pedidos.")
        else:
            print(f"Platos pedidos en la mesa {mesa}:")
            for item in pedidos[mesa]:
                print(f"- {item['nombre']}")

    # Esta es la función principal que gestiona las mesas
    def gestionar_mesa():
        while True:
            try:
                mesa = int(input("Selecciona una mesa (1-5) o 0 para salir: "))
                if mesa == 0:
                    break
                elif 1 <= mesa <= 5:
                    while True:
                        print(f"Gestión de la mesa {mesa}")
                        print("1. Asignar platos")
                        print("2. Mostrar cuenta total")
                        print("3. Mostrar platos pedidos")
                        print("4. Volver")
                        opcion = input("Selecciona una opción: ")

                        if opcion == "1":
                            asignar_pedido(mesa)
                        elif opcion == "2":
                            mostrar_cuenta(mesa)
                        elif opcion == "3":
                            mostrar_pedidos(mesa)
                        elif opcion == "4":
                            break
                        else:
                            print("Opción no válida.")
                else:
                    print("Mesa no válida, intenta nuevamente.")
            except ValueError:
                print("Entrada no válida. Intenta nuevamente.")

    # Función que funciona como menu principal del programa
    def main():
        print("Bienvenido a Almuerzos Dora UPB")
        input("Presiona Enter para entrar al programa...")
        
        while True:
            mostrar_mesas()
            gestionar_mesa()

    if __name__ == "__main__":
        main()

