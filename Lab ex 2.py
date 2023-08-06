#1.1
# Creating an empty list
my_list = []

# Using append() to add elements
my_list.append(47)
my_list.append('Priya')
my_list.append([13,4,3])

# Using insert() to add elements at specific positions
my_list.insert(1, 'BTS')
my_list.insert(2, 7)

# Using extend() to add elements from another iterable
my_list.extend([8, 9, 10])

# Adding a tuple to the list
my_list.append((12,6,13))

# Adding a set to the list
my_list.extend({95,97,94})

# Adding a dictionary to the list
my_list.append({'RM': 'Leader', 'JK': 'Maknae'})

# Printing the final list
print(my_list)


#1.2
# Create a list of numeric elements
numeric_list = [30, 9, 18, 1, 12, 13, 4]
print(numeric_list)

# Swap the first and last elements
def swap_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]

swap_first_last(numeric_list)
print("List after swapping first and last elements:", numeric_list)

# Find the sum of the digits in the list
def sum_of_digits(lst):
    total = 0
    for num in lst:
        total += sum(int(digit) for digit in str(num))
    return total

digit_sum = sum_of_digits(numeric_list)
print("Sum of digits in the list:", digit_sum)

# Find the smallest element in the list
def find_smallest(lst):
    if len(lst) == 0:
        return None
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

smallest_element = find_smallest(numeric_list)
print("Smallest element in the list:", smallest_element)

#2.1
# List of dictionaries
dict_list = [
    {'name': 'Rm', 'age': 28},
    {'name': 'Jin', 'age': 30},
    {'name': 'Suga', 'age': 30},
    {'name': 'Jhope', 'age': 29},
    {'name': 'Jimin', 'age': 27},
    {'name': 'V', 'age': 27},
    {'name': 'Jk', 'age': 25}
]

# Sort the list of dictionaries based on the 'name' key
sorted_dict_list = sorted(dict_list, key=lambda x: x['name'])

# Print the sorted list of dictionaries
for item in sorted_dict_list:
    print(item)

#2.2
# Create a dictionary with numeric values
numeric_dict = {
    'a': 28,
    'b': 30,
    'c': 30,
    'd': 29,
    'e': 27,
    'f': 27,
    'g': 25
}

# Calculate the sum of all values in the dictionary
total_sum = sum(numeric_dict.values())

# Print the sum
print("Sum of all values:", total_sum)
    
#2.3
# Dictionary with numeric values
numeric_dict = {
    'a': 92,
    'b': 93,
    'c': 94,
    'd': 95,
    'e': 97
}

# Sort the dictionary in descending order of values using a lambda function
sorted_dict_descending = dict(sorted(numeric_dict.items(), key=lambda item: item[1], reverse=True))

# Print the sorted dictionary
print("Sorted dictionary in descending order of values:")
for key, value in sorted_dict_descending.items():
    print(key, ':', value)
