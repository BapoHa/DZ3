import sys
from typing import Callable


def generator_numbers(text: str):
   
    for word in text.split():
        try:
            yield float(word)
        except ValueError:
            pass            # skip words that cannot be converted to float


def sum_profit(text: str, func: Callable) -> float:
    
    return sum(func(text))


def read_file(file_path: str) -> str:
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except OSError as e:
        print(f"Помилка читання файлу: {e}")
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 2:      # check if file path argument is provided
        print("Використання: python <шлях до DZ2_T8.py> <шлях_до_файлу>")
        sys.exit(1)

    file_path = sys.argv[1]

    text = read_file(file_path)

    print(f"Аналізується файл: {file_path}")
    print(" " * 20)

    print("Знайдені числа:")    # show found numbers
    for number in generator_numbers(text):
        print(f"  {number}")

    total_income = sum_profit(text, generator_numbers) # calculate total income using the generator function
    print(" " * 20)
    print(f"Загальний дохід: {total_income}")
