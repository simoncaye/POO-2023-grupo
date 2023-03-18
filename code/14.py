class departamento:
    
   
    def __init__(self, ventas, salario_vendedor):
        self.ventas = ventas
        self.salario_vendedor = salario_vendedor
        self.incentivo = 0.0
    
    
    def calcular_incentivo(self, ventas_totales):
        if self.ventas > ventas_totales * 0.33:
            self.incentivo = self.salario_vendedor * 0.2
        else:
            self.incentivo = 0.0
    
    
    def calcular_salario_total(self):
        salario_total = self.salario_vendedor + self.incentivo
        return salario_total


def ventas():
    
    ventas1 = float(input("Ingrese las ventas del departamento 1: "))
    ventas2 = float(input("Ingrese las ventas del departamento 2: "))
    ventas3 = float(input("Ingrese las ventas del departamento 3: "))
    salario_vendedor = float(input("Ingrese el salario mensual de los vendedores: "))
    
    
    ventas_totales = ventas1 + ventas2 + ventas3
    
    
    departamento1 = Departamento(ventas1, salario_vendedor)
    departamento2 = Departamento(ventas2, salario_vendedor)
    departamento3 = Departamento(ventas3, salario_vendedor)
    
    
    departamento1.calcular_incentivo(ventas_totales)
    departamento2.calcular_incentivo(ventas_totales)
    departamento3.calcular_incentivo(ventas_totales)
    salario_total1 = departamento1.calcular_salario_total()
    salario_total2 = departamento2.calcular_salario_total()
    salario_total3 = departamento3.calcular_salario_total()
    
    
    print(salario_total1)
    print(salario_total2)
    print(salario_total3)

ventas()