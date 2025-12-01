numbers = [12,10,7,9,56,8,5]
sum_of_odd = 0
index = 0

for count in numbers:
    if index % 2 != 0:
        sum_of_odd+=count
    index+=1
print(sum_of_odd)
