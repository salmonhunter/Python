class Mainbank:
    def __init__(self):
        self.money = 1000000
        self.interest = 0.02
        self.account = 1111

    def transfer(self, money, Person):
        self.money -= money
        Person.deposit(money)
        print(Person.name + "계좌로 " + format(money, ',') +"가 송금되었습니다.")
        print("은행잔액은 " + format(self.money, ',') + " 입니다.")

    def deposit(self, money, Person):
        self.money += money
        Person.transfer(money, Person.account)
        print(Person.name + " 계좌에서 " + format(money, ',') +"가 입금되었습니다.")
        print("잔액은 " + format(self.money, ',') + " 입니다.")


class Person:

 
    
    def __init__(self, name):
        self.money = 100000
        self.name = name
        self.account = 65252

    def transfer(self, money, account):
        self.money -= money
        print(self.name + "의 계좌에서 " + str(account) + "계좌에 " + format(money, ',') +"가 송금되었습니다.")
        print(self.name + "의 계좌잔액은 " + format(self.money, ',') + " 입니다.")

    def deposit(self, money):
        self.money += money
        print(format(money, ',') +"가 입금되었습니다.")
        print("잔액은 " + format(self.money, ',') + " 입니다.")





patrick = Person("Patrick")
bank1 = Mainbank()

bank1.transfer(1000000000, patrick)
bank1.deposit(10000000, patrick)
