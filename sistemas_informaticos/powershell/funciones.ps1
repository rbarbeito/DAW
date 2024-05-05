<# Crear funciones#>


function Crear-Fechas([Datetime]$FechaInicial,
                       [Datetime] $FechaFinal){

            $d=$FechaInicial

            while($d-le $FechaFinal){
                Write-Host $d
                $d =  $d.AddDays(1)
            }
}

#Crear-Fechas "1/1/2024" "1/3/2024"
Crear-Fechas -FechaFinal "2/13/2024" `
             -FechaInicial "2/10/2024"