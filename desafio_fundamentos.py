#!/usr/bin/env python3

#  desafio_fundamentos.py


class Bank_Account:

    _WITHDRAW_AMOUNT_LIMIT = 3
    _WITHDRAW_VALUE_LIMIT = 500
    __withdraw_amount = 0
    __bank_transition = []

    def __init__(self, balance = 0):
        self.__balance = balance

    def withdraw(self, value):
        if self.__withdraw_amount >= self._WITHDRAW_AMOUNT_LIMIT:
            print(f'Não será possivel sacar R$ {value:.2f}.',
                    "Excedido o número de saques.")
            return 2
        if value > self._WITHDRAW_VALUE_LIMIT:
            print("Não será possível sacar o dinheiro excedido o valor limite")
            return 3
        if value > self.__balance:
            print("Não será possivel sacar o dinheiro por falta de saldo")
            return 4

        self.__bank_transition.append(f"Saque: R$ {value:.2f}")
        self.__withdraw_amount += 1
        self.__balance -= value

        print(f"Sacado R$ {value:.2f}. Saldo restante R$ {self.__balance:.2f}")
        return 0

    def deposit(self, value):
        self.__balance += value
        print(f"Depositado R$ {value:.2f}. Novo saldo R$ {self.__balance:.2f}")
        self.__bank_transition.append(f"Depósito: R$ {value:.2f}")

        return 0

    def bank_statement(self):
        print("*** Extrato Bancário. ***")

        for transition in self.__bank_transition:
            print(transition)

        print()
        print("****************************")
        print()
        print(f"Saldo: R$ {self.__balance:.2f}.")

menu = """
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[q]\tSair

\t=>"""


cliente = Bank_Account()

while True :

    func = input(menu)

    if func == "d":
        value = input("Digite o valor de depósito: R$ ")
        cliente.deposit(float(value))

    elif func == "s":
        value = input("Digite o valor do saque: R$ ")
        cliente.withdraw(float(value))

    elif func == "e":
        cliente.bank_statement()

    elif func == "q":
        print("Saindo...")
        break



