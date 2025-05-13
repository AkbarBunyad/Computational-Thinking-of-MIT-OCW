import time

def fibonacci_naive(n):
    if n<=1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci_memo(n, memo = None):
    if memo is None:
        memo = {}
    if n<=1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def fibonacci_iterative(n):
    if n<=1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

n = 40
start = time.time()
fib_naive = fibonacci_naive(n)
end = time.time()
print(f"Fibonacci naive: {fib_naive} (time: {end-start:.6f} seconds)")

start = time.time()
fib_memo = fibonacci_memo(n)
end = time.time()
print(f"Fibonacci memo: {fib_memo} (time: {end-start:.6f} seconds)")    

start = time.time()
fib_iterative = fibonacci_iterative(n)
end = time.time()
print(f"Fibonacci iterative: {fib_iterative} (time: {end-start:.6f} seconds)")

