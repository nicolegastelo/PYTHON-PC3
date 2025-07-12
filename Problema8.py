import requests
import zipfile
import os

image_url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"


def descargar_imagen(url, nombre_archivo):
    try:
        
        response = requests.get(url)
        response.raise_for_status() 
        
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagen descargada y guardada como: {nombre_archivo}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

def crear_zip(nombre_archivo_imagen, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(nombre_archivo_imagen, os.path.basename(nombre_archivo_imagen))
        print(f"Archivo ZIP creado: {nombre_zip}")
    except Exception as e:
        print(f"Error al crear el archivo ZIP: {e}")

nombre_imagen = "imagen_descargada.jpg"
nombre_zip = "imagen_comprimida.zip"

descargar_imagen(image_url, nombre_imagen)

crear_zip(nombre_imagen, nombre_zip)
