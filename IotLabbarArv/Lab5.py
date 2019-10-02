from datetime import datetime
from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, date, number, customer):
        self._date = date
        self._number = number
        self._customer = customer
    
    @abstractmethod
    def confirm(self):
        pass

    @abstractmethod
    def close(self):
        pass

class SpecialOrder(Order):
    def __init__(self, date,number,customer):
        super().__init__(date,number,customer)

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


class Customer():
    def __init__(self, name, location):
        self._name = name
        self._location = location



c = Customer("Stefan", "Nacka")
c2 = Customer("Kerstin", "Nacka")

o1 = NormalOrder(datetime.now(),"123",c)
o2 = SpecialOrder(datetime.now(),"124",c)
o2 = NormalOrder(datetime.now(),"125",c2)

