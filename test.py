class Bank:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def moneyX(self, balance):
        cash = input("Введите сумму:")
        balance += cash
        print("Ваш баланс сотавляет:", cash)

    def _kill(self):  
        self.__balance = 0
        print("Весь баланс обнулен.")



    def __str__(self):
        return f'Ваш банк {self.__name}\n' \
               f'У вас на счёту: {self.__balance}'


bank1 = Bank("Мой банк", 100)
bank2 = Bank("Другой банк", 100)
print(bank1)
