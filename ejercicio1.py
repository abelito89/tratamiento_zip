import requests
from pathlib import Path
import logging
import os
import zipfile

# Configuración de las variables de entorno del proxy usando HTTP
os.environ['HTTP_PROXY'] = 'http://abel.gomez:Septiembre*2024@192.168.91.20:3128'
os.environ['HTTPS_PROXY'] = 'http://abel.gomez:Septiembre*2024@192.168.91.20:3128'

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

url = 'https://raw.githubusercontent.com/abelito89/zip/refs/heads/main/texto.zip'

# Directorio donde se guardará el archivo descargado
download_dir = Path("descargas")
local_file = download_dir / "texto.zip"
extracted_dir = download_dir / "extracted"

# Crear el directorio si no existe
if not download_dir.exists():
    _logger.debug(f"Creando directorio {download_dir}")
    download_dir.mkdir(parents=True, exist_ok=True)

def get_ftp(url: str) -> None:
    try:
        _logger.debug(f"Iniciando la descarga del archivo desde {url}")
        response = requests.get(url)
        response.raise_for_status()  # Verifica si hay errores HTTP
        _logger.debug(f"Guardando el archivo en {local_file}")
        with local_file.open("wb") as f:
            f.write(response.content)
        _logger.info(f"Archivo descargado exitosamente y guardado como {local_file}")
    except requests.exceptions.RequestException as e:
        _logger.error(f"Error al descargar el archivo: {e}")

def verify_zip(file: Path) -> bool:
    try:
        _logger.debug(f"Verificando el contenido del archivo {file}")
        with file.open("rb") as f:
            file_head = f.read(4)
            _logger.debug(f"Encabezado del archivo: {file_head}")

        # Verificar si el archivo descargado es realmente un zip
        if zipfile.is_zipfile(file):
            _logger.info(f"El archivo {file} es un archivo zip válido")
            return True
        else:
            _logger.error(f"El archivo {file} no es un archivo zip válido. Encabezado del archivo: {file_head}")
            return False
    except Exception as e:
        _logger.error(f"Error al verificar el archivo: {e}")
        return False

def extract_zip(file: Path, extract_to: Path) -> None:
    try:
        _logger.debug(f"Descomprimiendo el archivo {file}")
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        _logger.info(f"Archivo descomprimido exitosamente en {extract_to}")
    except zipfile.BadZipFile as e:
        _logger.error(f"Error al descomprimir el archivo: {e}")

def remove_file(file: Path) -> None:
    try:
        _logger.debug(f"Eliminando el archivo {file}")
        file.unlink()
        _logger.info(f"Archivo {file} eliminado exitosamente")
    except FileNotFoundError as e:
        _logger.error(f"Error al eliminar el archivo: {e}")

# Ejecución del proceso completo
get_ftp(url)
if verify_zip(local_file):
    extract_zip(local_file, extracted_dir)
    remove_file(local_file)
