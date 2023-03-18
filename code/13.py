class Almacen:
    def __init__(self, total_compra):
        self.total_compra = total_compra

    def calcular_descuento(self, bolita_color):
        
        descuento = 0

        
        if bolita_color == "blanca":
            descuento = 0
        elif bolita_color == "verde":
            descuento = 0.1
        elif bolita_color == "amarilla":
            descuento = 0.25
        elif bolita_color == "azul":
            descuento = 0.5
        elif bolita_color == "roja":
            descuento = 1

    
        cantidad_final = self.total_compra - (self.total_compra * descuento)

     
        return cantidad_final