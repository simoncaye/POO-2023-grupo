class empleado:
    
    def __init__(self, nombre, horasxsemana, pagoxhora):
        self.nombre = nombre
        self.horasxsemana = horasxsemana
        self.pagoxhora = pagoxhora

    def salario(self):
        pago = 0

        if 40 < self.horasxsemana <48:
            horasextra = self.horasxsemana - 40
            pagoextra = horasextra * 2
            pago = pagoxhora * self.horasxsemana + pagoextra
        
        if horasxsemana > 48:
            superextrahoras = self.horasxsemana - 48
            superpagoextra = superextrahoras * 3
            
            pagoextra2 = pagoxhora * 16
            pago = pagoxhora * self.horasxsemana + pagoextra2 + superpagoextra

        return pago

def trabajador():
    name = input()
    hour4week = int(input())
    paid4hour = int(input())

    dinerito = empleado(name, hour4week, paid4hour)

    print('El salario es', dinerito.salario)


trabajador()