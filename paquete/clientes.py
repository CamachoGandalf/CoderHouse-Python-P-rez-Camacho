#Clase cliente con atributos nombre, apellido, edad, dni, nacionalidad, direccion, telefono, email y nivel de comprador


class cliente:


    def __init__(self, nombre, apellido, edad, dni, nacionalidad, direccion, telefono, email, nivel_comprador):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.nacionalidad = nacionalidad
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.nivel_comprador = nivel_comprador
        self.lista_deseados = []
    

    def info(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Edad: ", self.edad)
        print("dni: ", self.dni)
        print("nacionalidad: ", self.nacionalidad)
        print("Dirección: ", self.direccion)
        print("Teléfono: ", self.telefono)
        print("Email: ", self.email)
        print("Nivel comprador: ", self.nivel_comprador)
        print("Lista deseados: ", self.lista_deseados)


    #Metodo subír de nivel con checks de descuento por nivel.
    def subir_nivel(self, nivel_comprador):
        nivel_anterior = self.nivel_comprador
        self.nivel_comprador += nivel_comprador
        print("nivel actual: ", self.nivel_comprador)
    
        # Verificar si alcanza niveles con descuentos
        if self.nivel_comprador >= 10 and nivel_anterior < 10:
            print("¡Felicidades! Has alcanzado el nivel 10 y ahora obtienes un 20 de descuento en todas tus compras.")
        elif self.nivel_comprador >= 7 and nivel_anterior < 7:
            print("¡Felicidades! Has alcanzado el nivel 7 y ahora obtienes un 15 de descuento en todas tus compras.")
        elif self.nivel_comprador >= 3 and nivel_anterior < 3:
            print("¡Felicidades! Has alcanzado el nivel 3 y ahora obtienes un 10 de descuento en todas tus compras.")


    def __str__(self):
        return f"\nHola, me llamo {self.nombre} {self.apellido}, tengo {self.edad} años, soy de {self.nacionalidad}, mis datos son \nDNI: {self.dni}.\ntelefono: {self.telefono}.\nmail: {self.email}.\nMi nivel de comprador y neceficios es: {self.nivel_comprador}."


    #Metodo comprar.   
    def comprar(self, cantidad, producto, tienda):
        return f"\nEl cliente {self.nombre} {self.apellido} compró {cantidad} {producto} en la tienda de {tienda}.\nLos detalles de la factura fueron enviados al mail {self.email}."


    #Agregar elementos a la wish list.
    def add_wish_list(self, productos):
        self.lista_deseados.append(productos)
        productos_list = ', '.join(productos)
        return f"{self.nombre} {self.apellido} ha agregado {productos_list} a la lista de deseos."
    

    #Ver elemetos de la lista de deseos en forma de lista.
    def ver_wish_list(self):
        if self.lista_deseados:
            print(f"Lista de deseos de {self.nombre} {self.apellido}:")
        for producto in self.lista_deseados:
            print("-", producto)
        else:
            print(f"La lista de deseos de {self.nombre} {self.apellido} está vacía.")


    #Eliminar elementos de la lista de deseos.
    def eliminar_de_wish_list(self, producto):
        if not self.lista_deseados:
            print(f"La lista de deseos de {self.nombre} {self.apellido} está vacía.")
        elif producto not in self.lista_deseados:
            print(f"El producto '{producto}' no está en la lista de deseos de {self.nombre} {self.apellido}.")
        else:
            self.lista_deseados.remove(producto)
            print(f"El producto '{producto}' ha sido eliminado de la lista de deseos de {self.nombre} {self.apellido}.")
