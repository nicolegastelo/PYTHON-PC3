class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None  
        self.notas = []  

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad:
            print(f"Edad: {self.edad}")
        else:
            print("Edad no asignada.")
        
        if self.notas:
            print(f"Notas: {', '.join(map(str, self.notas))}")
        else:
            print("No se han asignado notas.")
    
    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

nombre = input("Introduce el nombre del alumno: ")
numero_registro = input("Introduce el número de registro del alumno: ")

alumno = Alumno(nombre, numero_registro)

edad = int(input("Introduce la edad del alumno: "))
alumno.setAge(edad)

notas = input("Introduce las notas del alumno separadas por comas: ").split(",")
notas = [float(nota) for nota in notas]  

alumno.setNota(notas)

alumno.display()
