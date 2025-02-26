# syncmods
programa para sincronizar los archivos de una carpeta entre cliente y servidor

## Instalar entorno virtual
Instala un entorno virtual sobre el cual se van a instalar las dependencias y ejecutar el proyecto
```
python3 -m venv venv
```
## Activar el entorno virtual en Windows
Inicia un entorno virtual de python
```
venv\Scripts\activate
```
## Instalar requerimientos
Instala las dependencias para la ejecucion del proyecto
```
pip install -r requirements.txt
```
## Actualizar el archivo de requerimientos
Agrega las nuevas dependencias(librerias) instaladas al archivo de requerimientos
```
pip freeze > requirements.txt
```
# Ejecutar el proyecto
## ejecutar el proyecto en modo debug
```
uvicorn main:app --reload
```

## ejecutar el proyecto en modo produccion
```
uvicorn main:app --host x.x.x.x --port x
```
