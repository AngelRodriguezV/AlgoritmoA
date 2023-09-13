@echo off

:: Nombre del entorno virtual
set env_name=env

:: Verifica si el entorno virtual ya existe
if not exist %env_name%\ (
    :: Crea el entorno virtual
    python -m venv %env_name%
)

:: Activa el entorno virtual
call %env_name%\Scripts\activate

:: Instala las dependencias desde requirements.txt
pip install -r requirements.txt

:: Desactiva el entorno virtual
deactivate

echo Entorno virtual '%env_name%' creado y requerimientos instalados.
