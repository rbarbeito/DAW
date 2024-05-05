# Operador de asiganacion

$a=@(1,2,3,4,5,6,7)
$b=$a
$a[0]=6

Write-Host $a
Write-Host $b

$c=$a.clone()

$a[0]=10

Write-Host $c
Write-Host $a


