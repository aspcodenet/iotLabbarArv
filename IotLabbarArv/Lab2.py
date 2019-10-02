from abc import ABC, abstractmethod
from enum import Enum

class FoodType(Enum):
    FoodType_Vegetarisk = 1
    FoodType_Vegan = 2
    FoodType_Kott = 3

class Matratt:
    def __init__(self, name, price, type, calories):
        self._name = name
        self._price = price
        self._type = type
        self._calories = calories
        self._servedAtLunch = False
        self._servedAlacarte = False
    
    def GetName(self):
        return self._name

    def ServedAt(self, lunch, alaCarte):
        self._servedAtLunch = lunch
        self._servedAlacarte = alaCarte

    def IsServedAtLunch(self):
        return self._servedAtLunch 

    def IsServedAtAlacarte(self):
        return self._servedAlacarte


    def GetOriginalPrice(self):
        return  self._price


    def GetPrice(self, lunch):
        if lunch: 
            return  self._price
        return self._price * 1.7

    def GetType(self):
        return self._type.name

    def GetFoodType(self):
        return self._type


class MenyMatratt:
    def __init__(self, name, price, type):
        self._name = name
        self._price = price
        self._type = type

    def GetName(self):
        return self._name

    def GetPrice(self):
        return self._price

    def GetType(self):
        return self._type

class Meny(ABC):
    @abstractmethod
    def GenerateMenu(self, matrattLista):
        pass

class LunchMeny(Meny):
    def GenerateMenu(self, matrattLista):
        meny = []
        for mat in matrattLista:
            if mat.IsServedAtLunch():
                meny.append(MenyMatratt(mat.GetName(), mat.GetOriginalPrice(),mat.GetType()))
        return meny


class AlacarteMeny(Meny):
    def GenerateMenu(self, matrattLista):
        meny = []
        for mat in matrattLista:
            if mat.IsServedAtAlacarte():
                meny.append(MenyMatratt(mat.GetName(), mat.GetOriginalPrice()*1.7,mat.GetType()))
        meny.append(MenyMatratt("Ölbuffe", 199,""))
        return meny


m1 = Matratt("Spagetti Carbonara",99,FoodType.FoodType_Kott,100)
m2 = Matratt("Pannkakor",85,FoodType.FoodType_Vegetarisk,20)
m3 = Matratt("Ärtsoppa",60,FoodType.FoodType_Vegan,50)

matLista = [m1,m2,m3]
m1.ServedAt(True,True)
m2.ServedAt(True,False)
m3.ServedAt(False,True)


meny = LunchMeny()
print("Lunchmeny")
for l in meny.GenerateMenu(matLista):
    print(f"{l.GetName()} {l.GetType()} {l.GetPrice()}")

alacarteMeny = AlacarteMeny()
print("Alacartemeny")
for l in alacarteMeny.GenerateMenu(matLista):
    print(f"{l.GetName()} {l.GetType()} {l.GetPrice()}")





