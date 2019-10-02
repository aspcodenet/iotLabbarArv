from abc import ABC, abstractmethod

class Kattdjur(ABC):
    def __init__(self, artName, color):
        self._artname = artName
        self._color = color

    def GetArtName(self):
        return self._artname
    
    def GetColor(self):
        return self._color

    @abstractmethod
    def MakeSound():
        pass

class Tiger(Kattdjur):
    def __init__(self, color, isDangerous):
        super().__init__("Tiger",color)
        self._isDangerous = isDangerous

    def MakeSound(self):
        return f"Jag är en {self._isDangerous} {self._artname} och säger GRRRR" 
        

class Huskatt(Kattdjur):
    def __init__(self, color):
        super().__init__("Huskatt",color)

    def MakeSound(self):
        #return f"Jag är en {self.GetArtName()} och säger mjau" 
        return f"Jag är en {self._artname} och säger mjau" 


katt1 = Huskatt("Svart")
katt1.GetArtName()
katt2 = Huskatt("Vit")

tiger1 = Tiger("Randig")
djurLista = [ katt1, katt2, tiger1 ]

for djur in djurLista:
    print(djur.MakeSound())
