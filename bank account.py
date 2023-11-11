class Bank_account:

    def __init__(self, client_name, client_age, initial_balance=0):
        self.client_name = client_name
        self.client_age = client_age
        self.balance = initial_balance
        self.transactions = []


    def deposit(self, sum):
        self.balance += sum
        self.transactions.append(f"Пополнение: +{sum}")
        print(f'Ваш баланс был пополнен на: {sum}')

    def withdraw(self, sum):
        if sum > 0 and sum <= self.balance:
            self.balance -= sum
            self.transactions.append(f"Снятие: -{sum}")
            print(f'Вы сняли со счета: {sum}')
        elif sum <= 0:
            print("Сумма для снятия должна быть положительной.")
        else:
            print("Недостаточно средств на счете.")

    def get_info(self):
        print()
        print(f'Клиент: {self.client_name}, Возраст: {self.client_age}'
              f'\nБаланс: {self.balance}\nПоследние операции: {self.transactions}\n')


cliet1 = Bank_account('Oleg', 23, 0)
cliet1.deposit(1000)
cliet1.withdraw(500)
cliet1.get_info()
