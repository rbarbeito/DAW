# Guía de cómo deshacer el último commit con git.

1. Si no has hecho push:

- Para mantener cambios: `git reset --soft HEAD~1`
- Para eliminar cambios: `git reset --hard HEAD~1`
- Para arreglar el commit (mensaje o añadir cambios):
`git commit --amend -m "Mensaje corregido"`

2. Ya has hecho push:
- git revert <hash> para crear un nuevo commit que invierte los cambios. Si hay conflictos, prepárate para manejarlos.
- git log para recuperar el hash del commit que quieres revertir.

3. Nivel experto:
- `git rebase -i` para modificar tu historial de commits localmente. Puedes cambiar el orden, combinar, editar o eliminar commits.
- Luego ejecuta "`git push --force-with-lease`"

> 🚨 Aviso: Sólo usa rebase y push forzado en ramas donde seas el único colaborador o en situaciones donde todos los colaboradores estén al tanto y de acuerdo con reescribir la historia.
