"""Бібліотека математичних функцій без введення та виведення."""


def gcd(a, b):
    """Невід’ємний НСД цілих чисел за алгоритмом Евкліда."""
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Невід’ємний НСК через gcd; для нульового аргументу — 0."""
    g = gcd(a, b)
    if g == 0:
        return 0
    return abs(a // g * b)


def is_prime(n):
    """Перевірити, чи ціле число n є простим."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def factorial(n):
    """Факторіал невід’ємного цілого; для від’ємного — None."""
    if n < 0:
        return None
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def divide(a, b):
    """Частка a/b; при діленні на нуль повертає None."""
    if b == 0:
        return None
    return a / b


def power(x, n=2):
    """Додаткова вправа: степінь з цілим n; 0 у від’ємному степені — None."""
    if x == 0 and n < 0:
        return None
    return x ** n
