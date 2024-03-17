## Patrones usados en gitignore

Esta serie de patrones son usados en el archivo `.gitignore` para de una manera sencilla excluir archivos de proyectos muy grandes

|Patrón|Descripción|
|:---:|:---|
|*|Cualquier coincidencia en archivos|
|**|Cualquier coincidencia en carpetas|
|[abc]|Coincidencia, siempre que incluya uno de los caracteres dentro de los corchetes|
|?|Coincidencia, corresponde a un único carácter, `???` coincidencia con 3 caracteres|
|[0-9]|Coincidencia numérica, numero del 0 al 9|
|[a-z]|Coincidencia letras, solo las letras en minúsculas|
|[A-Z]|Coincidencia letras, solo las letras mayúsculas|
|[a-Z]|Coincidencia letras, Todas las letras pero no incluye las que representan códigos ASCII|
|*.a|Coincidencia, Todos los archivos con extension `.a`|
|!lib.a|Coincidencia, **NEGACIÓN** incluir el archivo, lib.a|
|.?TODO|Coincidencia, Ignora todo el archivo `TODO` de la carpeta raíz|
|build/|Coincidencia, ignora todo el contenido de la carpeta `build`|
|doc/notes.txt|Coincidencia, Ignora el archivo `notes.txt` dentro de la carpeta `doc`|
|!doc/server/arch.txt|Coincidencia, **NEGACIÓN** de exclusion del archivo `arch.txt` que se encuentra en la carpeta `doc/server/`|
|doc/**/*.txt|Coincidencia, Todos los archivos con extension `txt`, que se encuentren en cualquier directorio hijo de la carpeta `doc`, Aquí es como si realizara una búsqueda recursiva en toda la carpeta `doc`|