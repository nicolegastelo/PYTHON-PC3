def obtener_fraccion():
    while True:
        try:
            fraccion = input("Introduce una fracción en formato X/Y: ")
    
            x, y = fraccion.split("/")
            
            x = int(x)
            y = int(y)
            
            if x > y or y == 0:
                print("Error: X debe ser menor o igual a Y, y Y no puede ser 0.")
                continue
            
            porcentaje = (x / y) * 100
            
            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{round(porcentaje)}%")
            
            break
            
        except ValueError:
            print("Error: Solo se permiten números enteros.")
        except ZeroDivisionError:
            print("Error: Y no puede ser 0.")

obtener_fraccion()