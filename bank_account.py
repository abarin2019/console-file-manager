"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

def account_info(account):
    print(f"Ваш счет:  {account:.2f} руб")


def account_top_up():
    return float(input("На сколько хотите пополнить счет:  "))


def purchase(balance, history):
    purchase_price = float(input("Введите сумму покупки:  "))

    if purchase_price > balance:
        print(f"Вам не хватает денег на покупку")
    else:
        purchase_name = input("Введите название покупки:  ")
        balance -= purchase_price
        history.update({purchase_name: purchase_price})

    return balance, history

def purchase_history(history):
    print(f"\nИстория покупок: ")

    for key, value in history.items():
        print(f"{key}: {value:.2f} руб")


def use_bank_account():
    balance_account = 0
    account_history = {}

    while True:
        print()
        account_info(balance_account)
        print()
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')
        print()

        choice = input('Выберите пункт меню:  ')
        if choice == '1':
            balance_account += account_top_up()

        elif choice == '2':
            balance_account, account_history = purchase(balance_account, account_history)

        elif choice == '3':
            purchase_history(account_history)

        elif choice == '4':
            break

        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    use_bank_account()