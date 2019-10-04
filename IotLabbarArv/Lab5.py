from datetime import datetime
from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, date, number, customer):
        self._date = date
        self._number = number
        self._customer = customer
    
    def ChangeCustomerName(self, newName):
        self._customer.SetName(newName)


    @abstractmethod
    def confirm(self):
        pass

    @abstractmethod
    def close(self):
        pass

class SpecialOrder(Order):
    def __init__(self, date,number, customer):
        super().__init__(date,number, customer)

    def confirm(self):
        pass

    def close(self):
        pass

    def dispatch(self):
        pass



class NormalOrder(Order):
    def __init__(self, date,number, customer):
        super().__init__(date,number, customer)

    def confirm(self):
        pass

    def close(self):
        pass

    def dispatch(self):
        pass

    def receive(self):
        pass


class Customer:
    def __init__(self, name, location):
        self._name = name
        self._location = location

    def SetName(self, newName):
        self._name = newName

    def GetName(self):
       return self._name

    def sendOrder(self):
        pass

    def receiveOrder(self):
        pass
    


c = Customer("Stefan", "Nacka")
c2 = Customer("Kerstin", "Nacka")

o1 = NormalOrder(datetime.now(),"123",c)
o1.ChangeCustomerName("kalle")
print(c.GetName())

o2 = SpecialOrder(datetime.now(),"124",c)
o3 = NormalOrder(datetime.now(),"125",c2)

