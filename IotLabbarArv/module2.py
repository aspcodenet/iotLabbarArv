class Person:
    def __init__(self, personNummer):
        if len(personNummer) != 10:
            raise ValueError("10 tecken pucko")
        self._personNummer = personNummer

    def SetPersonNummer(self, personNummer):
        if len(personNummer) != 10:
            return False
        self._personNummer = personNummer
        return True




while True:
    try:
        personNr = input("Ange personnummer")
        p = Person(personNr)
        break
    except:
        print("Fel personnummer")        

    



def SafeGetInt():
    print(3/0)
    while True:
        try:
            varde = int(input())
            return varde
        except ex as ValueError:
            print(ex)







varde = SafeGetInt()
varde2 = SafeGetInt()
print("Nu dividerar vi")
try:
    print(f"{varde/varde2}")
except:
    print("Nåt gick fel. Ring supporten och skäll som tusan")
print("Klart")
