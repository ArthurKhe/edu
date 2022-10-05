def fib(n):
    """
    Функция-генератор чисел Фибоначчи
    :param n: количество чисел
    :return:
    """
    a = 0
    cur = 1
    yield a
    b = 1
    cur += 1
    yield b
    while cur <= n:
        c = a + b
        yield c
        cur += 1
        a = b
        b = c


try:
    fib = fib(10)
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
except StopIteration:
    print("Больше чисел не выдам)!")