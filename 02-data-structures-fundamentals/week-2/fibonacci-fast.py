# Efficient Algorithm for Fibonacci numbers

'''FibonacciIterative(n)
    create an array F[0... n]
    F[0] <- 0
    F[1] <- 1
    for i from 2 to n:
        F[i] <- F[i-1] + F[i-2]
    return F[n]

'''


def fibonacci_recurs(n):
    if (n <= 1):
        return n
    else:
        return fibonacci_recurs(n - 1) + fibonacci_recurs(n - 2)


def fibonacci_iter(n):
    # create an array F[0...n]
    fib = []
    fib.append(0)
    fib.append(1)

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


if __name__ == "__main__":
    print(fibonacci_iter(10))
