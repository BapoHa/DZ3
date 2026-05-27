def caching_fibonacci():
   
    cache = {}  # for storing previously computed Fibonacci numbers

    def fibonacci(n):
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) 
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()

    print("=== Калькулятор чисел Фібоначчі")

    while True:
        user_input = input("\nВведіть номер числа Фібоначчі (або 'exit' для виходу): ")

        if user_input.strip().lower() == ( "exit"): 
            print("До побачення!")
            break

        if not user_input.strip().isdigit(): # check if input is a non-negative integer
            print("Помилка: введіть ціле невід'ємне число.")
            continue

        n = int(user_input.strip())
        result = fib(n)
        print(f"Фібоначчі({n}) = {result}")
