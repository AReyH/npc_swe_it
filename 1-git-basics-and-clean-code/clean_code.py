# Example of bad code
def c(l):
    r = 0
    for i in l:
        if i % 2 == 0:
            r += i
    return r


# Example of clean code
def sum_even_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total


# Example of cleaner code
def sum_even_numbers(numbers: list[int]) -> int:
    """Returns the sum of all even numbers in a list."""
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

