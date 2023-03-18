from clases_actividad2 import *

def ejercicio18():
    codigo=input("Introduzca el codigo del Empleado\n")
    nombre=input("Introduzca el nombre del empleado\n")
    horas=input("Numero de horas trabajadas al mes\n")
    valorHora=input("Valor de hora trabajada\n")
    retencion=input("Porcentaje retencion en la fuente (%)\n")

    datos=ejercicio_18(int(codigo),nombre,int(horas),int(valorHora),float(retencion))
    datos.salarioEmpleado()

def ejercicio19():
    lado=input("Lado del triangulo equilatero \n")
    datos=ejercicio_19(float(lado))
    datos.Area()
    datos.Altura()
    datos.Perimetro()

def ejercicio21():
    lado1=input("Lado 1 del triangulo equilatero \n")
    lado2=input("Lado 2 del triangulo equilatero \n")
    lado3=input("Lado 3 del triangulo equilatero \n")

    datos=ejercicio_21(float(lado1),float(lado2),float(lado3))
    datos.Perimetro()
    datos.SemiPerimetro()
    datos.Area()

def ejercicio7():
    a=input("Ingrese el primer valor \n")
    b=input("Ingrese el segundo valor \n")

    datos=ejercicio_7(int(a),int(b))
    datos.desicion()

def ejercicio10():
    inscripcion=input("Ingrese Número de inscripción \n")
    nombre=input("Ingrese el nombre del estudiante \n")
    patrimonio=input("Ingrese el patrimonio del estudiante \n")
    estrato=input("Ingrese el estrato social del estudiante \n")

    datos=ejercicio_10(inscripcion,nombre,int(patrimonio),int(estrato))
    datos.pago()

def ejercicio11():
    a=input("Ingrese el primer numero\n")
    b=input("Ingrese el segundo numero\n")
    c=input("Ingrese el tercer numero\n")

    datos=ejercicio_11(int(a),int(b),int(c))
    datos.mayor()
ejercicio11()