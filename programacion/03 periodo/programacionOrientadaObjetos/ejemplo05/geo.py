class Geo:

    def __init__(self,lat,long):
        self.lat=lat
        self.long=long

    def is_hemiferio_norte(cls):
       return cls.lat<=0