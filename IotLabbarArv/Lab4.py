from abc import ABC, abstractmethod

class FordonsAnnons(ABC):
    def __init__(self, pris, rubrik, beskrivning, year, antalmil):
        self._pris = pris
        self._rubrik = rubrik
        self._beskrivning = beskrivning
        self._year = year
        self._antalmil = antalmil

    @abstractmethod
    def GetAnnonsText(self):
        pass

class BilAnnons(FordonsAnnons):
    def __init__(self, pris, rubrik, beskrivning, year, antalmil, color, summerTires, winterTires):
        super().__init__(pris, rubrik, beskrivning, year, antalmil)
        self._color = color
        self._summerTires = summerTires
        self._winterTires = winterTires
    def GetAnnonsText(self):
        s = f"""{self._rubrik} {self._color} {self._pris} kr
{self._beskrivning} Årsmodell: {self._year} Antal mil: {self._antalmil}"""

        if self._summerTires:    
            s = s + """
            Sommardäck ingår"""

        if self._winterTires:    
            s = s + """
            Vinterdäck ingår"""

        return s

class HusvagnsAnnons(FordonsAnnons):
    def __init__(self, pris, rubrik, beskrivning, year, antalmil, dusch, nrOfBeds):
        super().__init__(pris, rubrik, beskrivning, year, antalmil)
        self._dusch = dusch
        self._nrOfBeds = nrOfBeds

    def GetAnnonsText(self):
        s = f"""{self._rubrik} {self._pris} kr   Antal bäddar: {self._nrOfBeds}
{self._beskrivning} Årsmodell: {self._year} Antal mil: {self._antalmil}"""
        if self._dusch:    
            s = s + """
            Dusch ingår"""
        return s


class MotorCykelAnnons(FordonsAnnons):
    def __init__(self, pris, rubrik, beskrivning, year, antalmil, motorVolym, drivTyp):
        super().__init__(pris, rubrik, beskrivning, year, antalmil)
        self._motorVolym = motorVolym
        self._drivTyp = drivTyp

    def GetAnnonsText(self):
        s = f"""{self._rubrik} {self._pris} kr   Antal mil: {self._antalmil}
{self._beskrivning} Årsmodell: {self._year} Motorvolym: {self._motorVolym} Drivtyp: {self._drivTyp}"""
        return s


lista = []
lista.append(MotorCykelAnnons(12000,"En cool Honda mc","Riktigt snygg",2008,2100,"300","Kardan"))
lista.append(BilAnnons(120000,"Volvo XC90","Ett riktigt fynd, bara lindrigt krockskadad",2012,12100,"Blå",True, False))
lista.append(HusvagnsAnnons(4000,"Kabe hUSVAGN","Original",1972,22300,True, 8))

for annons in lista:
    print(annons.GetAnnonsText())
    print()

