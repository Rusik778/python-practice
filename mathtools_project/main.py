from mathtools import gcd, lcm, is_prime, factorial, divide, power

MENU = """
1 — НСД і НСК
2 — Перевірка простого числа
3 — Факторіал
4 — Ділення
5 — Піднесення до степеня
0 — Вихід
"""


def main():
    """Показувати меню, читати дані й викликати функції бібліотеки."""
    while True:
        print(MENU)
        choice = input("Ваш вибір: ")
        if choice == "0":
            print("Роботу завершено")
            break
        elif choice == "1":
            a = int(input("a = "))
            b = int(input("b = "))
            print("НСД =", gcd(a, b), "НСК =", lcm(a, b))
        elif choice == "2":
            n = int(input("n = "))
            if is_prime(n):
                print("Просте")
            elif n >= 2:
                print("Складене")
            else:
                print("Не є простим або складеним")
        elif choice == "3":
            n = int(input("n = "))
            result = factorial(n)
            if result is None:
                print("Число має бути невід’ємним")
            else:
                print("Факторіал:", result)
        elif choice == "4":
            a = float(input("a = "))
            b = float(input("b = "))
            result = divide(a, b)
            if result is None:
                print("Ділити на нуль не можна")
            else:
                print("Частка:", result)
        elif choice == "5":
            x = float(input("x = "))
            n = int(input("Цілий показник n = "))
            result = power(x, n)
            if result is None:
                print("Нуль у від’ємному степені не визначено")
            else:
                print("Степінь:", result)
        else:
            print("Невідомий пункт меню")


if __name__ == "__main__":
    main()
