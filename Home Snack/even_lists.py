numbers = [12,10,7,9,56,8,5]
sums = 0

for count in range(0,len(numbers),2):
    sums+=numbers[count]
print(sums)

sum_of_even = 0
index =0
for counter in numbers:
    if index % 2 == 0:
        sum_of_even += counter
    index+=1
print(sum_of_even)
