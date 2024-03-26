# Entornos virtuales

- Son carpetas aisladas del sistema operativo donde tendrán sus propios `pip list` de las librerías instaladas
- Permite tener diferentes versiones de python personalizadas para cada entorno de trabajo
- Deben ser activadas y desactivadas para trabajar con cada un a de ellas


1. se debe instalar un manejador de entornos virtuales

```python
pip install virtualenv
```

## Pasos para trabajo con un proyecto en un entorno virtual

1. Abrimos el `Git Bash`, asi garantizamos tener en windows la potencia de la consola de Linux.
2. Creamos una carpeta con el nombre del proyecto `mkdir <nombre_del_proyecto>`
3. Accedemos a la carpeta `cd <nombre_de_la_carpeta>`
4. Creamos el entorno virtual para el proyecto, definiendo un nombre, este nombre creara una nueva carpeta con la estructura necesaria para el eso del mismo 
```python
python -m venv <nombre_del_entorno>
```
5. Se acitva el entorno de trabajo `source ./<nombre_del_entorno>/Scripts/activate`

> 📑 **Nota:** Como estamos usando `Git Bash` que trabaja en el entorno `UNIX` se debe anteponer la `source`, si se utiliza la consola de windows, no es necesario esto

6. Para desactivar 

```python
source ./<nombre_del_entorno>/Scripts/deactivate
```

Cuando tenemos activado un entorno virtual de trabajo, en la consola aparece `(<nombre_del_entorno>)` sobre cada linea de comando que se vaya a ejecutar



## Solución de problemas encontrados

###### Al Activar un entorno, no reconoce el interprete de python instalado
1. Debemos buscar la ruta en nuestras variables de entorno que hacen referencia a nuestro interprete de pyhton y copiar la misma.
2. En la carpeta del proyecto ir a la carpeta con el entorno creado y buscar el archivo `pyenv.cfg`
3. Dentro del mismo editamos las siguientes lineas:
```
home =<url_python>
include-system-site-packages = false
version = 3.12.2
executable = <url_python>\python.exe
command = <url_python>\python.exe -m venv <url_del_entorno>
```

## Archivo `requirements`

Se puede generar un archivo requirements con los paquetes instalados en el entorno, similar al `package.json` de `nodejs`
```
 pip freeze > requirements.txt
```

Cuando debamos volver a instalar los paquetes después de clonar el repositorio desde git, podemos reconstruir los mismos
```
pip install -r requirements.txt
```

## Para recuperar el proyecto despues de optener una copia desde GIT

1. Descargamos el proyecto desde GIT
2. creamos un entorno virtual de trabajo `python -m venv <nombre_del_entorno>`
3. activamos el entorno
4. Instalamos los paquetes del archivo de `requeriments.txt` con este comando `pip install -r requirements.txt`