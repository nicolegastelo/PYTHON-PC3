class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

largo = float(input("Introduce el largo del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))
rectangulo = Rectangulo(largo, ancho)

lado = float(input("Introduce el lado del cuadrado: "))
cuadrado = Cuadrado(lado)

area_rectangulo = rectangulo.calcular_area()
area_cuadrado = cuadrado.calcular_area()

print(f"Área del rectángulo: {area_rectangulo}")
print(f"Área del cuadrado: {area_cuadrado}")

