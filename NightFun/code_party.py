from functools import reduce

tuple_of_numbers = (10, 20, 30, 40, 50)

def append_number_to_tuple(tuple, num):
    return tuple + (num,)

new_tuple = append_number_to_tuple(tuple_of_numbers, 60)
print(new_tuple)

numbers=(1, 2, [3, 4], 5)

def change_third_element_first_value(tuple, new_value):
    tuple[2][0] = new_value
    return tuple

modified_tuple = change_third_element_first_value(numbers, 99)
print(modified_tuple)

tuple_of_strings = ("apple", "banana", "cherry")

def convvert_tuple_to_list_and_add_string_and_convert_back(tuples, string):
    temp_list = list(tuples)
    temp_list.append(string)
    return tuple(temp_list)

new_tuple_of_strings = convvert_tuple_to_list_and_add_string_and_convert_back(tuple_of_strings, "date")
print(new_tuple_of_strings)

this_tuple = (10, 20, 30, 40)

def unpack_and_print_tuple(tuples):
    a, b, *others = tuples
    print(f"a: {a}, b: {b}, others: {others}")

unpack_and_print_tuple(this_tuple)

sample_list = [ [2, 3, 4], [1, 5, 7], [4, 6, 8] ]

def sum_inner_elements_of_2d_list(list_2d):
    row_sums = []
    for row in list_2d:
        row_sums.append(sum(row))
    return (row_sums)

print(sum_inner_elements_of_2d_list(sample_list))

list_of_numbers = [ [2, 3, 4], [1, 5, 7], [4, 6, 8] ]

def sum_all_elements_in_corresponding_index(list_2d):
    result = []
    total = 0
    for count in range(len(list_2d[0])):
        for row in list_2d:
            total += row[count]
        result.append(total)
        total = 0
    return result
print(sum_all_elements_in_corresponding_index(list_of_numbers))

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

def even_numbers_from_1_to_21(list_of_numbers):
    return list_of_numbers % 2 == 0
print(list(filter(even_numbers_from_1_to_21, list_of_numbers)))

animals = ['cat', 'elephant', 'tiger', 'lion']
def animals_with_more_than_three_characters(animal_list):
    return len(animal_list) > 5
print(list(filter(animals_with_more_than_three_characters, animals)))

list_of_tuples = [(1, 'A'), (4, 'B'), (2, 'C')]

def tuples_with_first_element_greater_than_two(tuple_list):
    return tuple_list[0] > 2
print(list(filter(tuples_with_first_element_greater_than_two, list_of_tuples)))

def numbers_between_range_1_and_51_divisible_by_3_and_5(numbers):
    return 1 < numbers < 51 and numbers % 3 == 0 and numbers % 5 == 0
print(list(filter(numbers_between_range_1_and_51_divisible_by_3_and_5, range(1, 51))))

def palindrome_checker(string_list):
    return string_list == string_list[::-1]
print(list(filter(palindrome_checker, ['radar', 'hello', 'level', 'world', 'madam'])))

def convert_strings_list_to_uppercase_using_map(strings_list):
    return list(map(str.upper, strings_list))
print(convert_strings_list_to_uppercase_using_map(['apple', 'banana', 'cherry']))

def square_numbers_from_1_to_10_using_map(numbers_list):
    return numbers_list ** 2
squared_numbers = list(map(square_numbers_from_1_to_10_using_map, range(1, 11)))
print(squared_numbers)

def capitalize_first_letter_of_each_word_using_map(strings_list):
    return strings_list.capitalize()
capitalized_words = list(map(capitalize_first_letter_of_each_word_using_map, ['hello world', 'python programming', 'map function']))
print(capitalized_words)

def add_10_percent_tax_to_prices_using_map(prices_list):
    return prices_list * 1.10
prices_with_tax = list(map(add_10_percent_tax_to_prices_using_map, [100, 200, 300, 400, 500]))
print(prices_with_tax)  

def sum_all_numbers_between_1_and_50_using_reduce(numbers_list,numbers):
    return numbers_list + numbers
total_sum = reduce(sum_all_numbers_between_1_and_50_using_reduce, range(1, 51))
print(total_sum)

def maximum_number_in_list_using_reduce( number_one, number_two):
    return number_one if number_one > number_two else number_two
max_number = reduce(maximum_number_in_list_using_reduce, [5, 12, 8, 21, 3, 17])
print(max_number)

def concatenate_strings_in_list_using_reduce(strings_list, string):
    return strings_list + ' ' + string
concatenated_string = reduce(concatenate_strings_in_list_using_reduce, ['Hello', 'world!', 'Welcome', 'to', 'reduce', 'function.'])
print(concatenated_string)

def square_numbers_using_map(numbers_list):
    return numbers_list ** 2
squared_numbers_map = list(map(square_numbers_using_map, [1, 2, 3, 4]))

def multiply_numbers_using_reduce(number_one, number_two):
    return number_one * number_two
product_of_numbers = reduce(multiply_numbers_using_reduce, squared_numbers_map)
print(product_of_numbers)

tuples=[(1, 2), (3, 4), (5,6)]
def sum_elements_of_tuple(tuple_data):
    return sum(tuple_data)
summed_tuples = list(map(sum_elements_of_tuple, tuples))

def greater_than_five(tuple_data):
    return tuple_data > 5
filtered_tuples = list(filter(greater_than_five, summed_tuples))
print(filtered_tuples)

def non_numeric_strings(string_data):
    return  string_data.isnumeric()
non_numeric_filtered = list(filter(non_numeric_strings, ['123','789', 'abc', '456', 'def']))

def convert_strings_to_integers(string_data):
    return int(string_data)

integer_strings = list(map(convert_strings_to_integers, non_numeric_filtered))

def sum_of_integers(number_one, number_two):
    return number_one + number_two
total_integer_sum = reduce(sum_of_integers, integer_strings)
print(total_integer_sum)