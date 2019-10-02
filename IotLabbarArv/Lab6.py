class Account:
    def __init__(self,kontonummer):
        self._kontonummer = kontonummer
        self._saldo = 0

    def GetKontoNummer(self):
        return self._kontonummer

    def Withdraw(belopp):
        if self._saldo < belopp:
            return False
        self._saldo -= belopp
        return True

    def Deposit(belopp):
        self._saldo += belopp

    def GetSaldo(belopp):
        self._saldo += belopp

class User:
    def __init__(self, username,password):
        self._username = username
        self._password = password
        self._accounts = []

    def AddAccount(self,accountNumber):
        self._accounts.append(Account(accountNumber))

    def GetAccountNumbers(self):        
        list = []
        for acc in self._accounts:
            list.append(acc.GetKontoNummer())
        return list

    def GetAccount(self,accountNumber):        
        for acc in self._accounts:
            if acc.GetKontoNummer() == accountNumber:
                return acc
        return None
        
    
a = User("stefan", "nafets")
a.AddAccount("12345")
a.AddAccount("44455")

for s in a.GetAccountNumbers():
    print(s)



