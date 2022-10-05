import time


def mark_the_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(f"Время выполнения функции: {time.time() - start_time} sec")
        return res
    return wrapper


@mark_the_time
def foo(n, v):
    time.sleep(n)
    return n, v


