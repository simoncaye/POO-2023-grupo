class mayor:
    def __init__(self):
        self.valores = []
        for i in range (3):
            valor = int(input('ingresa el valor'))
            self.valores.append(valor)
        
    def comparar(self):
        valores = self.valores
        mayor = 0
        for valor in valores:
            if (valor>mayor):
                mayor = valor
        print("el mayor es ", mayor)
