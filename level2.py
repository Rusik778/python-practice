"""Рівень 2: рекурсія, НСД, дроби та цифри числа."""


def factorial_iter(n):
    """Факторіал невід’ємного цілого циклом; для n < 0 — None."""
    if n < 0:
        return None
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def factorial_rec(n):
    """Факторіал рекурсією з базою n <= 1."""
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


def fib_iter(n):
    """Число Фібоначчі з індексом n, обчислене циклом."""
    if n < 0:
        return None
    a, b = 0, 1
    for k in range(n):
        a, b = b, a + b
    return a


def fib_rec(n):
    """Число Фібоначчі з індексом n, обчислене рекурсією."""
    if n < 0:
        return None
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


# Рекурсивна версія повторно обчислює ті самі значення у двох гілках.
# Кількість викликів зростає експоненційно, а fib_iter виконує n кроків.


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


def is_coprime(a, b):
    """Взаємна простота чисел означає gcd(a, b) == 1."""
    return gcd(a, b) == 1


def reduce_fraction(num, den):
    """Скоротити дріб; знаменник результату додатний, den=0 дає None."""
    if den == 0:
        return None
    g = gcd(num, den)
    num //= g
    den //= g
    if den < 0:
        num = -num
        den = -den
    return num, den


def digit_sum_rec(n):
    """Рекурсивна сума цифр невід’ємного цілого; n < 0 дає None."""
    if n < 0:
        return None
    if n < 10:
        return n
    return n % 10 + digit_sum_rec(n // 10)


def reverse_number(n):
    """Розвернути невід’ємне число; кінцеві нулі зникають."""
    if n < 0:
        return None
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r


def is_palindrome_number(n):
    """Перевірити числовий паліндром через reverse_number."""
    if n < 0:
        return False
    return n == reverse_number(n)


if __name__ == "__main__":
    for n in range(11):
        assert factorial_iter(n) == factorial_rec(n)
    print("Факторіали для 0–10 збігаються")
    print("Факторіал 5:", factorial_rec(5))
    print("Фібоначчі 10:", fib_iter(10), fib_rec(10))
    print("НСД і НСК:", gcd(12, 18), lcm(12, 18))
    print("Взаємно прості:", is_coprime(7, 13))
    print("Скорочений дріб:", reduce_fraction(12, 18))
    print("Сума цифр:", digit_sum_rec(50525))
    print("Число навпаки:", reverse_number(5072))
    print("Паліндром:", is_palindrome_number(12321))
