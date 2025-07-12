import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

circulo1 = Circulo(5)  
circulo2 = Circulo(10)  

area1 = circulo1.calcular_area()
area2 = circulo2.calcular_area()

print("Área del círculo 1 con radio", circulo1.radio, "es:", round(area1, 2))
print("Área del círculo 2 con radio", circulo2.radio, "es:", round(area2, 2))
