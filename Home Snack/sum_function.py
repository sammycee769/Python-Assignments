def sum_first_middle_last(number):
    first = number[0]
    last = number[-1]
    n = 0
    for _ in number:     
        n += 1
    if n % 2 == 1:  
        middle_index = n // 2
        middle = number[middle_index]
    else:
        mid1 = number[(n // 2) - 1]
        mid2 = number[n // 2]
        middle = (mid1 + mid2) / 2
    result = first + middle + last

    return result

numbers = [10, 20, 30,1, 40, 50]
print(sum_first_middle_last(numbers))
