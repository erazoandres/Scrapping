from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# Configurar Selenium con Chrome en modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar sin abrir ventana
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")



# Inicializar WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL de la página de Éxito
url = "https://www.exito.com/mercado/despensa"

# Abrir la página
driver.get(url)
time.sleep(5)  # Esperar a que la página cargue

# Capturar imágenes y nombres de productos
try:
    product_grid = driver.find_element(By.CLASS_NAME, "product-grid_fs-product-grid___qKN2")
    img_elements = product_grid.find_elements(By.TAG_NAME, "img") 
    h3_elements = product_grid.find_elements(By.TAG_NAME, "h3")

    imagenes_filtradas = [img for img in img_elements if img.get_attribute("alt") == "Imagen del producto"]


    # Extraer datos
    productos = []
    for img, h3 in zip(imagenes_filtradas, h3_elements):
        productos.append({
            "nombre": h3.text.strip(),
            "imagen": img.get_attribute("src")
        })

    # Mostrar resultados
    for index, producto in enumerate(productos, start=1):
        print(f"{index}. {producto['nombre']} -> {producto['imagen']}")

    # Suponiendo que 'productos' es la lista de diccionarios que capturaste
    productos_json = json.dumps(productos, indent=4, ensure_ascii=False)

    # Guardar en un archivo .json
    with open("./web scrapping/productos.json", "w", encoding="utf-8") as file:
        file.write(productos_json)

    print("Archivo 'productos.json' guardado exitosamente.")

    

except Exception as e:
    print("Error al obtener los productos:", e)

# Cerrar el navegador
driver.quit()
