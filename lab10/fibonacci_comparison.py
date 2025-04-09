import time

def recur_fibo(n):
    if n <= 1:
        return n
    return recur_fibo(n - 1) + recur_fibo(n - 2)

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def memo_fibo(n):
    if n <= 1:
        return n
    return memo_fibo(n - 1) + memo_fibo(n - 2)

n = 35

start = time.time()
print("Standard:", recur_fibo(n))
print("Time:", time.time() - start, "seconds")

start = time.time()
print("Memoized:", memo_fibo(n))
print("Time:", time.time() - start, "seconds")
