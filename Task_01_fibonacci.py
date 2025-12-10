def caching_fibonacci():
    cache = {}

    def fibonacci(n):         # базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if n in cache:      # якщо вже обчислювали це n — повертаємо з кешу
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)    # рекурсія + повертаємо число
        return cache[n]

    return fibonacci     

"""
Test: 
fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(15))  # 610
"""
