#1
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_list(n):
    return list(map(fibonacci, range(1,n+1)))

print(fibonacci_list(10))

