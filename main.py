# Funciones para la interfaz de consola:
from clases.inventario import Inventario
from clases.producto import Producto
from clases.venta import Venta
from clases.cliente import Cliente
from clases.mascota import Gato, Perro


def registrar_mascota():
    tipo = input("Ingrese el tipo de mascota (Gato/Perro): ").strip().lower()
    nombre = input("Nombre de la mascota: ")
    edad = int(input("Edad de la mascota: "))
    salud = input("Estado de salud de la mascota: ")
    precio = float(input("Honorarios de atención: "))

    if tipo == "perro":
        raza = input("Raza del perro: ")
        nivel_de_energia = input("Nivel de energía del perro: ")
        mascota = Perro(nombre, edad, salud, precio, raza, nivel_de_energia)
    elif tipo == "gato":
        raza = input("Raza del michi: ")
        independencia = input("Nivel de independencia del michi: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Aún no trabajamos con ese tipo de mascotas, ¡Lo sentimos!")
        return
    return mascota


def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    direccion = input("Dirección del cliente: ")
    telefono = input("Teléfono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente


def registrar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto: ")
    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad de producto: "))
    except ValueError:
        print("Error: Ingrese valores numéricos para el precio y la cantidad.")
        return None
    # precio = float(input("Precio del producto: "))
    # cantidad = int(input("Cantidad de producto: "))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto


def registrar_venta(clientes, inventario):
    nombre_cliente = input("Nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return

    productos = []

    while True:
        nombre_producto = input("Nombre del producto (deje vacío para finalizar): ")
        if not nombre_producto:
            break
        producto = next(
            (p for p in inventario.lista_de_productos if p.nombre == nombre_producto),
            None,
        )
        if producto:
            productos.append(producto)
        else:
            print("Producto no encontrado.")

    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print("La venta ha sido registrada exitosamente.")
    else:
        print("No se han registrado productos para la venta.")


# Menú


def mostrar_menu():
    print("\n --- Menú de gestión de El Jardín de Haku ---")
    print("1. Registrar Mascota")
    print("2. Registrar Cliente")
    print("3. Registrar Producto")
    print("4. Registrar Venta")
    print("5. Mostrar información acerca de Mascotas")
    print("6. Mostrar información acerca de Clientes")
    print("7. Mostrar información acerca de Productos")
    print("8. Generar alerta de inventario")
    print("9. Salir")


def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("\n Seleccione una opción: ")

        if opcion == "1":
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("Mascota registrada correctamente.")

        elif opcion == "2":
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("Cliente registrado correctamente.")

        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print("Producto registrado correctamente.")

        elif opcion == "4":
            registrar_venta(clientes, inventario)

        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())

        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_informacion())

        elif opcion == "7":
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_informacion())

        elif opcion == "8":
            umbral_minimo = int(input("Ingrese la cantidad mínima del inventario: "))
            print(inventario.generar_alerta(umbral_minimo))

        elif opcion == "9":
            print("Saliendo del sistema, ¡Gracias por usar la Haku app!")
            break
        else:
            print(
                "Opción no válida, por favor intente nuevamente con un número del 1 al 9, gracias."
            )


if __name__ == "__main__":
    main()
