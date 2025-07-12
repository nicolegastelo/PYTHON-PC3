import requests

# Función para obtener los datos del tipo de cambio
def obtener_tipo_cambio(year):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?year={year}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta fue exitosa (código 200)
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return None

# Función para calcular las fechas con las condiciones solicitadas
def analizar_datos_tipo_cambio(data):
    if not data:
        return None

    fechas_min_compra = []
    fechas_max_venta = []
    fechas_max_diferencia = []

    min_compra = float('inf')
    max_venta = -float('inf')
    max_diferencia = -float('inf')

    # Analizamos los datos de cada día
    for dia in data:
        fecha = dia['fecha']
        compra = dia['compra']
        venta = dia['venta']
        diferencia = venta - compra

        # Encontramos la fecha con el valor mínimo de compra
        if compra < min_compra:
            min_compra = compra
            fechas_min_compra = [fecha]
        elif compra == min_compra:
            fechas_min_compra.append(fecha)

        # Encontramos la fecha con el valor máximo de venta
        if venta > max_venta:
            max_venta = venta
            fechas_max_venta = [fecha]
        elif venta == max_venta:
            fechas_max_venta.append(fecha)

        # Encontramos la fecha con la diferencia de compra-venta máxima
        if diferencia > max_diferencia:
            max_diferencia = diferencia
            fechas_max_diferencia = [fecha]
        elif diferencia == max_diferencia:
            fechas_max_diferencia.append(fecha)

    return {
        'fechas_min_compra': fechas_min_compra,
        'fechas_max_venta': fechas_max_venta,
        'fechas_max_diferencia': fechas_max_diferencia
    }

# Función principal para ejecutar el análisis
def main():
    year = 2025
    datos = obtener_tipo_cambio(year)

    if datos:
        resultado = analizar_datos_tipo_cambio(datos)
        if resultado:
            print(f"Fechas con el valor mínimo de compra del dólar: {resultado['fechas_min_compra']}")
            print(f"Fechas con el valor máximo de venta del dólar: {resultado['fechas_max_venta']}")
            print(f"Fechas con la diferencia máxima de compra-venta: {resultado['fechas_max_diferencia']}")
        else:
            print("No se pudo analizar los datos.")
    else:
        print("No se pudieron obtener los datos de la API.")

if __name__ == '__main__':
    main()
