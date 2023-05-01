# Write a Python function that takes two arguments (a and b) and returns their sum.
def add(a, b):
    return a + b
result = 40+60
print(result)

# Write a Python function that takes a string as input and returns the string reversed.
def reverse_string(input_string):
    return input_string[::-1]
result = reverse_string("hello world")
print(result)

# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
result = sum_list([1, 2, 3, 4, 5])
print(result)

# Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
def remove_even(numbers):
    return [num for num in numbers if num % 2 != 0]
result = remove_even([1, 2, 3, 4, 5, 6])
print(result)


# Write a Python function that takes a list of integers as input and returns the highest value in the list.
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
result = find_max([1, 5, 3, 9, 4])
print(result)

# Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.
def capitalize_strings(strings):
    return [s.capitalize() for s in strings]
result = capitalize_strings(['apple', 'banana', 'cherry'])
print(result)