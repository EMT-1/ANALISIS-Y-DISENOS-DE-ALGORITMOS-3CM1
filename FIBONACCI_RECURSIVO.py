def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    fibonacci = fib(15)
    print('Fibonacci:')
    print(fibonacci)
    