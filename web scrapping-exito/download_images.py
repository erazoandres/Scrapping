import json
import requests
import os

# Cargar el JSON desde un archivo
with open("./web scrapping/imagenes.json", "r", encoding="utf-8") as file:
    imagenes = json.load(file)

# Crear carpeta para guardar las imágenes
os.makedirs("./web scrapping/imagenes_descargadas", exist_ok=True)

# Descargar cada imagen
for img in imagenes:
    nombre = img["nombre"]
    url = img["imagen"]

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Verificar errores

        # Guardar la imagen
        with open(f"./web scrapping/imagenes_descargadas/{nombre}.jpg", "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"✅ {nombre} descargada con éxito")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al descargar {nombre}: {e}")
