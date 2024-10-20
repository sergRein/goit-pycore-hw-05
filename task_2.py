import re
from typing import Callable

def generator_numbers(text: str)->list:
    numbers_pattern = r"\s(-?\d+\.*\d*)\s"
    for number in re.findall(numbers_pattern,text):
        yield float(number)


def sum_profit(text: str, func: Callable):
    total = 0.0
    for number in func(text):
        total += number

    return round(total,2)

text = "Загальний дохід працівника складається з -23.33 декількох 22 частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")