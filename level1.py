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


if __name__ == "__main__":
    print(c_to_f(100))
    print(triangle_area(6, 4))
    print(min_max(4, 9, 2))
