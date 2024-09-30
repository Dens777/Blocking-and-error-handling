import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance=0
        self.lock=threading.Lock()

    def deposit(self):
        for i in range(100):
            value=randint(50,500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance+=value
            print(f'Пополнение: {value}. Баланс: {self.balance}.')
            sleep(0.002)

    def take(self):
        for i in range(100):
            value=randint(50,500)
            print(f'Запрос на {value}')
            if self.balance>=value:
                self.balance-=value
                print(f'Снятие: {value}. Баланс: {self.balance}')
                sleep(0.001)
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
                sleep(0.002)

bk=Bank()
th1=threading.Thread(target=Bank.deposit,args=(bk,))
th2=threading.Thread(target=Bank.take,args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()