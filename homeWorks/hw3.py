class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        additional_money = float(input("Введите сумму для добавления на счет: "))
        self._balance += additional_money

    def _kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def _merge_balance(self, other):
        self._balance += other._balance


client1 = Bank("Client1", 100)
client2 = Bank("Client2", 100)

print("Баланс Client1:", client1._balance)
print("Баланс Client2:", client2._balance)

client1._kill()
print("Баланс Client1 после обнуления:", client1._balance)


client1._merge_balance(client2)
print("Баланс Client1 после объединения:", client1._balance)
print("Баланс Client2 после объединения:", client2._balance)
