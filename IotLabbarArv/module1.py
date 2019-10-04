from enum import Enum

class FoodType(enum):
    Vegetarisk = 1
    Vegan = 2
    Kott = 3



class Matratt:
    def __init__(self,namn,pris, typ):
        self._namn = namn
        self._pris = pris
        self._typ = typ

    def GetTyp(self):
        return self._typ
    def GetNamn(self):
        return self._namn

m1 = Matratt("Taco",99,FoodType.Kott)
m2 = Matratt("Ärtsoppa",80,FoodType.Vegetarisk)

lista = [m1,m2]

########### tusentals rader bort i en annan fil i galaxen
m3 = Matratt("Pannkaka",80,FoodType.Vegetarisk)


########### tusentals rader bort i en annan fil i galaxen

for mat in lista:
    if mat.GetTyp() == FoodType.Vegetarisk:
        print(mat.GetNamn())






















