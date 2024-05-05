<# Crear funciones#>


function Crear-Fechas{

      param([Datetime]$FechaInicial,[Int]$Dias=1)

            $d=$FechaInicial

            

       while($d -le $FechaFinal){
                $d #Valores de retorno
                $d =  $d.AddDays($Dias)
            }
}

#Crear-Fechas "1/1/2024" "1/3/2024"
$a = Crear-Fechas "1/1/2024" 

#$a = Crear-Fechas -FechaFinal "2/13/2024" `
#                    -FechaInicial "2/10/2024"


Write-Host $a $a.count