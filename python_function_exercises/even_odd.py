def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False


def is_odd(number):
    if (number % 2) != 0:
        return True
    else:
        return False

# print(is_even(4))
# print(is_even(75))
# print(is_odd(11))
# print(is_odd(42))

def only_evens(numbers):
    i = 0
    even_numbers = []
    while i < len(numbers):
        if (numbers[i] % 2) == 0:
            even_numbers.append(numbers[i])
        i = i + 1
    return even_numbers

def only_odds(numbers):
    i = 0
    odd_numbers = []
    while i < len(numbers):
        if (numbers[i] % 2) != 0:
            odd_numbers.append(numbers[i])
        i = i + 1
    return odd_numbers

print(only_odds([11, 20, 42, 97, 23, 10]))

print(only_evens([11, 20, 42, 97, 23, 10]))
