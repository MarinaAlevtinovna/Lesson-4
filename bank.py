class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f'Вы успешно пополнили счет. Сумма на счету - {self.balance}')

    def withdraw(self, money):
        if money > self.balance:
            print(f'Недостаточно средств на счету')
        elif money <= self.balance:
            self.balance -= money
            print(f'Вы успешно сняли {money} рублей. Остаток на счете {self.balance}')

    def all_balance(self):
        print(f'Текущий баланс - {self.balance}')

man = Account( 111111, 200)

man.all_balance()
man.deposit(1000)
man.withdraw(500)
man.withdraw(300)
man.all_balance()