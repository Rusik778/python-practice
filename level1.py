"""Рівень 1 практичної роботи П3. Руслан Чухно, МІТ-1026а."""


def c_to_f(c):
    """Перевести градуси Цельсія у Фаренгейти."""
    return c * 9 / 5 + 32


def triangle_area(a, h):
    """Площа трикутника за невід’ємними основою та висотою."""
    return a * h / 2


def min_max(a, b, c):
    """Повернути пару мінімуму й максимуму без min та max."""
    lo = a
    hi = a
    if b < lo:
        lo = b
    if c < lo:
        lo = c
    if b > hi:
        hi = b
    if c > hi:
        hi = c
    return lo, hi


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


def primes_up_to(n):
    """Надрукувати прості числа до n включно; повертає None."""
    for k in range(2, n + 1):
        if is_prime(k):
            print(k, end=" ")
    print()


def print_box(width, symbol="*", height=3):
    """Надрукувати порожню рамку; width і height >= 2, символ один."""
    if width < 2 or height < 2 or len(symbol) != 1:
        return
    print(symbol * width)
    for row in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)
    print(symbol * width)


def f_to_c(f):
    """Обернене перетворення температури, додаткова вправа."""
    return (f - 32) * 5 / 9


def rectangle_area(a, b):
    """Площа прямокутника, додаткова вправа."""
    return a * b


def count_primes(n):
    """Кількість простих чисел до n через is_prime."""
    count = 0
    for k in range(2, n + 1):
        if is_prime(k):
            count += 1
    return count


if __name__ == "__main__":
    print("100 C =", c_to_f(100), "F")
    print("Площа трикутника:", triangle_area(6, 4))
    lo, hi = min_max(4, 9, 2)
    print("Мінімум:", lo, "Максимум:", hi)
    primes_up_to(30)
    print_box(4)
    print_box(3, "#")
    print("Обернене перетворення:", f_to_c(c_to_f(25)))
    print("Площа прямокутника:", rectangle_area(3, 5))
    print("Простих до 20:", count_primes(20))
