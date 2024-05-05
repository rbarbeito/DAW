$colores=@("Azul","verde","Rojo")

foreach($c in $colores){
    Write-Host $c

    if($c -eq "verde"){break}
    }

