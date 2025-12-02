def sum_of_third_element(numbers):
    total = 0
    for index in range(2,len(numbers),3):
        total += numbers[index]
    return total
my_list = [5, 10, 20, 7, 9, 3, 4, 8, 6]
print(sum_of_third_element(my_list))


def sum_every_third(numbers):
    total = 0
    index = 1   
    for count in numbers:
        if index % 3 == 0:  
            total += count
        index += 1

    return total
print(sum_every_third(my_list))
