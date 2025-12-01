numbers = [12,10,7,9,56,8,5]
smallest = numbers[0] 
#index = 0
for count in numbers:
    if count < smallest:
        smallest = count
print(smallest)
