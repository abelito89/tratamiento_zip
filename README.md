# Script para Descargar, Verificar, Descomprimir y Eliminar Archivos ZIP

Este script permite descargar un archivo `.zip` desde una URL pública, verificar su validez, descomprimir el archivo en un directorio específico y finalmente eliminar el archivo `.zip`.

## Descripción

El script realiza las siguientes acciones:
1. **Descarga**: Descarga un archivo `.zip` desde una URL proporcionada.
2. **Verificación**: Verifica que el archivo descargado sea un archivo `.zip` válido.
3. **Descompresión**: Descomprime el archivo `.zip` en un directorio especificado.
4. **Eliminación**: Elimina el archivo `.zip` descargado, dejando solo los archivos descomprimidos.

## Requisitos

- Python 3.6 o superior
- Librerías: `requests`, `pathlib`, `logging`, `os`, `zipfile`

## Instalación de Dependencias

Puedes instalar las dependencias necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
