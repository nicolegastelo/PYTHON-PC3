
try:
    from pyfiglet import Figlet
except ImportError:
    import os
    print("La librería 'pyfiglet' no está instalada. Procederemos a instalarla.")
    os.system('pip install pyfiglet')
    from pyfiglet import Figlet

import random  

figlet = Figlet()

fuentes_disponibles = figlet.getFonts()

fuente_seleccionada = input(f"Seleccione una fuente (de las disponibles, o presione Enter para aleatoria): ")

if not fuente_seleccionada:
    fuente_seleccionada = random.choice(fuentes_disponibles)
    print(f"Fuente seleccionada aleatoriamente: {fuente_seleccionada}")

while fuente_seleccionada not in fuentes_disponibles:
    print("Fuente no válida, por favor elige una fuente de la lista disponible.")
    fuente_seleccionada = input(f"Seleccione una fuente de la lista: ")

figlet.setFont(font=fuente_seleccionada)

texto_imprimir = input("Ingrese el texto que desea convertir: ")

print(figlet.renderText(texto_imprimir))
