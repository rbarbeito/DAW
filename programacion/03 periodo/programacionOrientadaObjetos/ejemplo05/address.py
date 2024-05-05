from geo import Geo

class Address:

    def __init__(self, street, suite, city,zipcode, lat, long):
       self.street=street
       self.suite=suite
       self.city=city
       self.zipcode=zipcode
       self.geo=Geo(lat,long)

    def is_valencia(cls):
        return cls.city=="Valencia"


