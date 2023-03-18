import math 
class ecuacion:
    def __init__(self):
        self.valores = []
        for i in range (3):
            valor = int(input('ingresa el valor'))
            self.valores.append(valor)
        

    def solucion(self):
        valores = self.valores
        resultado1 = (valores[1]+math.sqrt((valores[1]**2)-(4*valores[0]*valores[2])))/(2*valores[0])
        resultado2 = (valores[1]-math.sqrt((valores[1]**2)-(4*valores[0]*valores[2])))/(2*valores[0])
        pint(resultado1, resultado2)
