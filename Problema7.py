# Intentar importar pyfiglet, si no está instalado, instalarlo
try:
    from pyfiglet import Figlet
except ImportError:
    import os
    print("La librería 'pyfiglet' no está instalada. Procederemos a instalarla.")
    os.system('pip install pyfiglet')
    from pyfiglet import Figlet

import random  # Necesitamos importar random para elegir una fuente aleatoria

# Crear una instancia de la clase Figlet
figlet = Figlet()

# Obtener la lista de fuentes disponibles
fuentes_disponibles = figlet.getFonts()

# Solicitar al usuario el nombre de la fuente
fuente_seleccionada = input(f"Seleccione una fuente (de las disponibles, o presione Enter para aleatoria): ")

# Si el usuario no ingresa una fuente, se elige una aleatoriamente
if not fuente_seleccionada:
    fuente_seleccionada = random.choice(fuentes_disponibles)
    print(f"Fuente seleccionada aleatoriamente: {fuente_seleccionada}")

# Asegurarse de que la fuente seleccionada esté entre las disponibles
while fuente_seleccionada not in fuentes_disponibles:
    print("Fuente no válida, por favor elige una fuente de la lista disponible.")
    fuente_seleccionada = input(f"Seleccione una fuente de la lista: ")

# Establecer la fuente en el objeto Figlet
figlet.setFont(font=fuente_seleccionada)

# Solicitar al usuario el texto a convertir en arte ASCII
texto_imprimir = input("Ingrese el texto que desea convertir: ")

# Imprimir el texto utilizando la fuente seleccionada
print(figlet.renderText(texto_imprimir))
