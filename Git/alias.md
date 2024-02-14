# Alias en GIT

Los alias son abreviaciones de uno o varios comandos de git, incluso lineas de comandos.
Con ello se ahorra tiempo y se reduce la posibilidad de equivocarse al escribir largas líneas en la consola de Git.

📢 EJEMPLO PARA CONFIGURAR ALIAS:

```bash
git config --global alias.estatus status
git config --global alias.revisar checkout
git config --global alias.descartar "checkout -- ."
```

🔊 USO DE LOS ALIAS:

```bash
git estatus
git revisar dev
git revisar master
git descartar
```


🔊 VER LISTA DE ALIAS:

```bash
git config --get-regexp alias
```

CONFIGURAR ALIAS PARA VER LISTA DE ALIAS:

```bash
git config --global alias.alias "config --get-regexp alias"

# Ejemplo: 
git alias //Devuelve la lista de alias.
```

🔊 CONFIGURAR ALIAS PARA CONFIGURA ALIAS

```bash
git config --global alias.configurar "config --global"

# Ejemplo: 
git configurar alias.estatus status 

#Crea el alias estatus para comando status, queda $ git estatus
```

🔊 ALIAS MÁS USADOS (simplificando creación con $ git configurar ...):

```bash
git configurar alias.clonar clone               
# Ej. git clonar git@github.com:bumptech/glide.git

git configurar alias.crear "checkout -b"        
# Ej. $ git crear ramaX

git configurar alias.subir "push origin"          
# Ej. $ git subir dev

git configurar alias.bajar "pull origin"          
# Ej. $ git bajar callings

git configurar alias.agregar "add . "             
# Ej. $ git agregar

git configurar alias.cometer "commit -m "         
# Ej. # git cometer "Cambios del commit"

git configurar alias.unir merge                   
# Ej. $ git unir --no-ff feature/lorem-ipsum

git configurar alias.eliminar "branch -d "        
# Eliminar ramaX Ej. git eliminar ramaX

git configurar alias.eliminarr "branch -dr "      
# Eliminar rama remota Ej: git eliminarr ramaX

git configurar alias.ramas "branch --list"        
# Listar nombre de ramas Ej. $ git ramas
```


🔊 BORRANDO UN ALIAS:
```bash
git config --global --unset alias.[tuAlias]
```

🔊 ALIAS PARA BORRAR ALIAS:
```bash
git configurar alias.borrar "config --global --unset" 
# Ejemplo de uso, $ git borrar alias.estatus
```


🔊 OTROS ALIAS ÚTILES:
```bash
git config --global alias.configuraciones "config --list"   
# Muestra las configuraciones de git

git config --global alias.alias "config --get-regexp alias" 
# Lista los alias existentes

git config --global alias.borrar "config --global --unset"  
# Borra un alias
```