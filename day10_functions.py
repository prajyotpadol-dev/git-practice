def greet(name, city="Mumbai"):
    print(f"{name} lives in {city}")


def add(a, b):
    return a + b


def square(number):
    return number ** 2


def is_even(number):
    return number % 2 == 0


def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def sum_even(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total


def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count


def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


# Test the functions
greet("Prajyot", "Pune")
greet("Rahul")

print("Addition:", add(10, 5))
print("Square:", square(6))
print("Is 8 even?", is_even(8))
print("Sum:", calculate_sum([5, 15, 25, 35, 45]))
print("Sum of even numbers:", sum_even([2, 5, 8, 11, 14, 3]))
print("Count of even numbers:", count_even([2, 5, 8, 11, 14, 3]))
print("Count of positive numbers:", count_positive([-2, 5, 0, 8, -1, 3]))
print("Largest number:", find_largest([12, 45, 7, 89, 23]))