from address import Address

class AlumnosDAW:

    def __init__(self, name, username, email, phone, website, street, suite, city,zipcode, lat, long):
        self.name=name
        self.username=username
        self.email=email
        self.phone=phone
        self.website=website
        self.address=Address(street,suite,city,zipcode, lat, long)



alumno1=AlumnosDAW("Jordi", "sapingo", "sapingo@gmail.com","6776544344","http://sapingo.com","Cortes valencianas",532,"Valencia","43116",23.1568,0.15687)

print("El alumno {} vive en estas coordenadas -> lat {} long {}".format(alumno1.name, alumno1.address.geo.lat, alumno1.address.geo.long))

print(alumno1.address.geo.is_hemiferio_norte())

print(alumno1.phone)

print(alumno1.address.is_valencia())

