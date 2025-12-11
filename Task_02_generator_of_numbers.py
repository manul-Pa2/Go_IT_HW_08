import re
from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]:     # створюємо генератор

    pattern = r"\d+(?:\.\d+)?"      # Шукаємо цілі та дробові числа

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:   # знаходимо всі числа в тексті і повертаємо їх значення
    return sum(func(text))


if __name__ == "__main__":          # числа трохи змінив
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1888.01 як основний дохід, доповнений додатковими "
        "надходженнями 57.75 і 684.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")        
    print(f"Загальний дохід: {total_income:.2f}")   
