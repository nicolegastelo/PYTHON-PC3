import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

radio1 = float(input("Introduce el radio del primer círculo: "))
radio2 = float(input("Introduce el radio del segundo círculo: "))

circulo1 = Circulo(radio1)
circulo2 = Circulo(radio2)

area1 = circulo1.calcular_area()
area2 = circulo2.calcular_area()

print(f"Área del primer círculo con radio {circulo1.radio}: {area1:.2f}")
print(f"Área del segundo círculo con radio {circulo2.radio}: {area2:.2f}")
