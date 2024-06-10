def fibonacci (n):
    if n <= 1:
        return n
    
    # inisiasi tabel
    fib = [0] * (n + 1)
    fib[1] = 1

    # mengisi tabel
    for i in range(2, n+1):
        fib[i] = fib[i -1 ] + fib [i - 2]

    return fib[n]


# contoh penggunaan
print(f"fibonacci {fibonacci(10)}")