from paquete.clientes import cliente
from paquete.productos import Producto
from paquete.login import registro, acceso, Menu

productosss = ["tomate", "otra cosa", "verduras"]
cliente1 = cliente("jose", "Pérez", 33, 40878785, "Argentina", "Calle falsa123", 123456789, "jose@gmail.com", 1)

cliente1.info
cliente1.subir_nivel(1)
cliente1.comprar(4, "manzanas", "verduleria de marito")
print(cliente1)

cliente1.add_wish_list(productosss)
cliente1.ver_wish_list()
# cliente1.eliminar_de_wish_list("tomate")


