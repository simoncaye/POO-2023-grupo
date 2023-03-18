class empleado:
    def __init__(self):
        self.nombre = input('Ingrese nombre')
        self.salario = float(input('Salario'))
        self.horas = float(input('Horas'))
    
    def pobre(self):
        nombre = self.nombre
        salario = self.salario
        horas = self.horas
        total = salario * horas
        if(total >= 450000):
            print(nombre)
            print(total)
        else:
            print(nombre)