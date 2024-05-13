#Clase producto con atributos nombre, id, precio y stock


class Producto:
    def __init__(self, nombre, id, precio, stock):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.stock = stock
    