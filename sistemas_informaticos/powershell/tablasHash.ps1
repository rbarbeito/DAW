<# Tablas hash#>

$a=@{forma="Cuadrado"; color="Azul"}

Write-Host $a
Format-Table -InputObject $a


<#Acceso a  valores
by keys or by .

#>


write-host $a["forma"]
write-host $a.forma


Write-Host $a.keys
Write-Host $a.values
Write-Host $a.count

<# adicionado new Keys#>

$a["forma"]=circulo
$a.color="verde"


<# Nuevo elemento.Operadores 
[] ó . ó +=
#>

$a["Coordenadas"]=10,20
$a.escala="1:1000"
$a += @{rotacion=45; sombra=$true; dolar=$null; comida=$false}

<#Eliminar elementos#>

$a.remove("color")

Format-Table -InputObject $a

$m=$a.clone()

$m["rosca"]="izq"

Format-Table -InputObject $a
Format-Table -InputObject $m




