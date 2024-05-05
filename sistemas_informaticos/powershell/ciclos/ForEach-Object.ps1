$colores=@("Azul","verde","Rojo")


Write-Output $colores | ForEach-object {
    Write-Host $_
    }


Write-Host ""


Get-ChildItem -Path C:\Windows\System32 *.dll | ForEach-Object {

# if ($_.Name -eq "xmlfilter.dll") {
    Write-Host El tamaño de $_.Name es $_.Length
#    }
}
 
