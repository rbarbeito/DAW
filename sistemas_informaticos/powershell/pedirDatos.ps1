<#
Pedir datos al usuario
#>

$a= Read-Host " Como te llamas"

Write-Host "Hola $a, bienvenido a mi powershell"


[int]$a = Read-Host "Dame un numero"

$a *= 2
Write-Host "Tu numero es ahora un $a"