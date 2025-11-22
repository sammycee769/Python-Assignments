sum_of_multiples = 0
for multiples in range(0,20000):
    if (multiples % 10 == 0):
        sum_of_multiples += multiples
print(f"The sum of the multiples of 10 in 20,000 is {sum_of_multiples}")
