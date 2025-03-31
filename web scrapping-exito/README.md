# Proyecto de Web Scraping con Selenium

Este repositorio contiene un script en Python que utiliza Selenium para hacer web scraping de productos en la página de Éxito.

## Requisitos

- Python 3.x
- Google Chrome
- Chromedriver
- Las siguientes librerías de Python:
  - `selenium`
  - `webdriver_manager`

## Instalación

1. Clona este repositorio:
   ```sh
   git clone <URL_DEL_REPO>
   cd <NOMBRE_DEL_REPO>
   ```
2. Instala las dependencias:
   ```sh
   pip install selenium webdriver-manager
   ```

## Uso

Ejecuta el script con el siguiente comando:
```sh
python script.py
```

El script guardará los datos de los productos en un archivo JSON ubicado en `./web scrapping/productos.json`.

## Notas

- El script usa el modo headless de Chrome para ejecutarse sin abrir una ventana gráfica.
- Se recomienda usar un entorno virtual de Python para evitar conflictos de dependencias.

## Licencia

Este proyecto está bajo la licencia MIT.
