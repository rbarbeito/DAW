usuario={
    "nombre":"",
    "edad":"",
    "direccion":"",
    "telefono":""
}

for key in usuario:
    dato=input("Teclee su " + key +  ": ")
    usuario[key]=dato
    
print(usuario["nombre"],"tiene",usuario["edad"],"años, vive en",usuario["direccion"], "y su número de teléfono es",usuario["telefono"])