# Программа вычисления факториала числа
# Практическая работа № 2, ветвь main

def factorial(n: int) -> int:
    """Возвращает факториал числа n."""
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    for num in range(0, 6):
        print(f"{num}! = {factorial(num)}")
