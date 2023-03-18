import math

#EJERCICIOS PRPUESTOS CAP 3

class ejercicio_18():
    def __init__(self,Codigo,nombre,horas,valorHora,retencion):
        self.Codigo=Codigo
        self.nombre=nombre
        self.horas=horas
        self.valorHora=valorHora
        self.retencion=retencion
    def salarioEmpleado(self):
        codigo=self.Codigo
        nombre=self.nombre
        horas=self.horas
        valorHora=self.valorHora
        retencion=self.retencion
        salarioBruto=valorHora*horas
        porcentaje=retencion/100
        salarioNeto=salarioBruto-(salarioBruto*porcentaje)
        print("Codigo de Empleado: "+str(codigo))
        print("Nombre de Empleado: "+str(nombre))
        print("Salario Bruto: "+str(salarioBruto))
        print("Salario Neto: "+str(salarioNeto))
class ejercicio_19():
    def __init__(self,lado):
        self.lado=lado
    def Area(self):
        lado=self.lado
        Area=(math.sqrt(3)*(lado*lado))/4
        Area=round(Area,2)
        print("Area: "+str(Area))
    def Altura(self):
        lado=self.lado
        Altura=(math.sqrt(3)*lado)/2
        Altura=round(Altura,2)
        print("Altura: "+str(Altura))
    def Perimetro(self):
        lado=self.lado
        Perimetro=3*lado
        Perimetro=round(Perimetro,2)
        print("Perimetro: "+str(Perimetro))
class ejercicio_21():
    def __init__(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def Perimetro(self):
        lado1=self.lado1
        lado2=self.lado2
        lado3=self.lado3
        Perimetro=lado1+lado2+lado3
        Perimetro=round(Perimetro,2)
        print("Perimetro: "+str(Perimetro))
    def SemiPerimetro(self):
        lado1=self.lado1
        lado2=self.lado2
        lado3=self.lado3
        SemiPerimetro=(lado1+lado2+lado3)/2
        SemiPerimetro=round(SemiPerimetro,2)
        print("SemiPerimetro: "+str(SemiPerimetro))
    def Area(self):
        lado1=self.lado1
        lado2=self.lado2
        lado3=self.lado3
        S=(lado1+lado2+lado3)/2
        Area=math.sqrt(S*(S-lado1)*(S-lado2)*(S-lado3))
        Area=round(Area,2)
        print("Area: "+str(Area))
      
#EJERCICIOS RESUELTOS CAP 4

class ejercicio_7():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def desicion(self):
        a=self.a
        b=self.b
        if a > b:
            print(str(a)+" Es mayor que "+str(b))
        elif a < b:
            print(str(a)+" Es menor que "+str(b))
        else:
            print(str(a)+" Es igual que "+str(b))
class ejercicio_10():
    def __init__(self,Inscripcion,nombres,Patrimonio,Estrato,):
        self.Inscripcion=Inscripcion
        self.nombres=nombres
        self.Patrimonio=Patrimonio
        self.Estrato=Estrato
    def pago(self):
        Inscripcion=self.Inscripcion
        nombres=self.nombres
        Patrimonio=self.Patrimonio
        Estrato=self.Estrato

        valor=50000
        if Patrimonio>2000000 and Estrato>3:
            valor=(Patrimonio*0.03)+valor

        print("El estudiante con numero de inscripcion "+str(Inscripcion)+" Y nombre "+str(nombres)+" Debe pagar "+str(valor))
class ejercicio_11():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def mayor(self):
        a=self.a
        b=self.b
        c=self.c
        lista=[a,b,c]
        mayor=0
        for i in range (len(lista)):
            if lista[i]>mayor:
                mayor=lista[i]
        print("El mayor de los 3 numeros es "+str(mayor))


