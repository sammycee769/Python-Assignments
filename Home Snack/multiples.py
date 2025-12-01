numbers = [12,10,7,9,56,8,5]
multiples = 1
index = 0

for count in numbers:
    if index % 3 == 0:
        multiples*=count
    index+=1
print(multiples)
