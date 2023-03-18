class pelotas:
    def __init__(self, peso):
        self.peso = peso


def cualpesamas():
    bola1 = int(input())
    bola2 = bola1 
    bola3 = bola2
    bola4 = int(input())

    if bola4 > bola1:
        print('La bola D es de mayor tamaño que el resto')
    if bola4 < bola1:
        print('La bola D es de menor tamaño que el resto')