class Calificaciones:
    def __init__(self):
        self.calificaciones = []

    def obtener_calificaciones(self):
        while True:
            try:
                calificaciones_input = input("Introduce las calificaciones separadas por comas: ")
                
                calificaciones_lista = calificaciones_input.split(",")
                
                self.calificaciones = [int(calificacion) for calificacion in calificaciones_lista]
                
                print("Las calificaciones ingresadas son:", self.calificaciones)
                break  
                
            except ValueError:
                print("Error: Todas las calificaciones deben ser números enteros.")

calificaciones_obj = Calificaciones()

calificaciones_obj.obtener_calificaciones()
