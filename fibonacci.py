from decorators import mark_the_time


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
    while cur < n:
        c = a + b
        yield c
        cur += 1
        a = b
        b = c


@mark_the_time
def ten_fib(n):
    lst = []
    fibo = fib(n)
    for i in range(n):
        lst.append(next(fibo))
    return lst


print(ten_fib(10))

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