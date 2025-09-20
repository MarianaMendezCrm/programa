class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("EL PRECIO Y LA CANTIDAD DEBEN SER POSITIVOS.")
            return

        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                print("YA EXISTE ESE PRODUCTO.")
                return

        nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.productos.append(nuevo_producto)
        print(f"PRODUCTO '{nombre}' AGREGADO CORRECTAMENTE.")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if cantidad <= 0:
                    print("LA CANTIDAD A VENDER DEBE SER POSITIVA.")
                    return
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f"VENTA REALIZADA: {cantidad} UNIDAD(ES) '{nombre}'.")
                else:
                    print("NO HAY SUFICIENTE STOCK PARA REALIZAR LA VENTA.")
                return
        print("PRODUCTO NO ENCONTRADO EN EL INVENTARIO.")

    def mostrar_inventario(self):
        print(f"\n INVENTARIO DE {self.nombre_tienda}:")
        if not self.productos:
            print("EL INVENTARIO ESTA VACIO.")
        else:
            for producto in self.productos:
                print(f"- {producto['nombre']}: ${producto['precio']} | STOCK: {producto['cantidad']}")

    def producto_mas_caro(self):
        if not self.productos:
            print("NO HAY PRODUCTOS EN EL INVENTARIO.")
            return
        producto_caro = max(self.productos, key=lambda p: p["precio"])
        print(f"\n PRODUCTO MAS CARO: {producto_caro['nombre']} (${producto_caro['precio']})")



def menu():
    tienda = InventarioTienda("TIENDA ESCOLAR")

    while True:
        print("\n OPCIONES:")
        print("1. AGREGAR PRODUCTO")
        print("2. VENDER PRODUCTO")
        print("3. VER INVENTARIO")
        print("4. CONSULTAR PRODUCTO MAS CARO")
        print("5. SALIR")

        opcion = input("SELECCIONA UNA OPCION (1-5): ")

        if opcion == "1":
            nombre = input("NOMBRE DEL PRODUCTO: ")
            try:
                precio = float(input("PRECIO DEL PRODUCTO: "))
                cantidad = int(input("CANTIDAD DISPONIBLE: "))
                tienda.agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("USA NUMEROS  PARA PRECIO Y CANTIDAD.")

        elif opcion == "2":
            nombre = input("NOMBRE DEL PRODUCTO A VENDER: ")
            try:
                cantidad = int(input("CANTIDAD A VENDER: "))
                tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print("USA NUMEROS ENTEROS PARA LA CANTIDAD.")

        elif opcion == "3":
            tienda.mostrar_inventario()

        elif opcion == "4":
            tienda.producto_mas_caro()

        elif opcion == "5":
            print("HASTA LUEGO")
            break

        else:
            print("OPCION NO VALIDA.")


menu()