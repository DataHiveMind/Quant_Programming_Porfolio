def Recursion1(n : int) -> int:   # Factorial by iteration
    result = 1
    while(n > 1):
        result = result * n
        n -= 1
    return result

def factR(n : int) -> int:  # Factorial by recursion
    if n == 1:
        return n
    else:
        return n * factR(n-1)   # Recursion - calling factR

def fib(n : int) -> int: # Fibonacci numbers
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # Recursion 1

def testFib(n : int):
    for i in range(n+1):
        print("FIb of ", i, '=', fib(i) ) # Recursion 2


if __name__ == "__main__":
    num = int(input("Enter a Number: "))

    # Recursion1
    print("Recursion1 Result: ", Recursion1(num))

    # factR
    print("FactR Result: ", factR(num))

    # fib
    print("Fib Result: ", fib(num))

    # testFib
    print("TestFib Result: ", testFib(num))




