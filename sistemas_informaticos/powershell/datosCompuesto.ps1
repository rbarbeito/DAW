<#Datos compuestos#>


<#Array

Valores separados por coma

@() permite crear arrays de 0 a 1 elemento

#>

$a=1,2,3,4,5,6
$b=@()
$c=@(1)
$d=@(1,2,3,4,5,6)

Write-Host $a
Write-Host $b
Write-Host $c
Write-Host $d

<#Array

Operador indice
primer indice: 0
ultimo indice: array.count -1
ultimo indice:  -1
tamaño del array:  array.count

#>


Write-Host $d.count
Write-Host $d[0]
Write-Host $d[-1]
Write-Host $d[$d.count -1]


<#Array
Añadir elementos
#>

Write-Host $a

$a += 6
$a += @(7,8,9)
$a += 10,11,12

Write-Host $a

<#Array
Operadores de comparacion
-In
-Contains
-NotIn
-NotContains
#>

$a = 1 -in @(1,2,3)
$b = @(1,2,3) -contains 1

$c = 6 -notin @(1,2,3)
$d = @(1,2,3,4) -notcontains 6

Write-Host $a
Write-Host $b
Write-Host $c
Write-Host $d

<#
Array de objetos de multipes tipos restringible con [tipo[]]
#>

$a=@(1,2,3,4,"Hola","Adios")
[int[]]$b=@(1,2,3,"Hola", "Adios")
[int[]]$c=(1,2,3,4,5,6)

Write-Host $a
Write-Host $b
Write-Host $c