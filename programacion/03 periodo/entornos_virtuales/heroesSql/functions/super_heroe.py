class SuperHeroe:

    __count = 0
    __good = 0
    __bad = 0
    __neutro = 0
    __desconocido = 0
    __marvel_comic = 0
    __dc_comics = 0

    def __init__(self, dt):
        (self.name,
         self.gender,
         self.eye,
         self.race,
         self.hair,
         self.height,
         self.publisher,
         self.skin,
         self.alignment,
         self.weight) = dt
        SuperHeroe.__count += 1
        SuperHeroe.contar_publisher(self)
        SuperHeroe.contar_alignment(self)

    def contar_publisher(cls):
        if cls.publisher == "Marvel Comics":
            SuperHeroe.__marvel_comic += 1
        elif cls.publisher == "DC Comics":
            SuperHeroe.__dc_comics += 1
        else:
            pass

    def contar_alignment(cls):
        if cls.alignment == "good":
            SuperHeroe.__good += 1
        elif cls.alignment == "bad":
            SuperHeroe.__bad += 1
        elif cls.alignment == "neutral":
            SuperHeroe.__neutro += 1
        else:
            SuperHeroe.__desconocido += 1

    def getCount():
        return SuperHeroe.__count

    def getCountMarvelComic():
        return SuperHeroe.__marvel_comic

    def getCountDcComic():
        return SuperHeroe.__dc_comics

    def getCountGood():
        return SuperHeroe.__good

    def getCountBad():
        return SuperHeroe.__bad

    def getCountNeutral():
        return SuperHeroe.__neutro

    def getCountUnKnow():
        return SuperHeroe.__desconocido
