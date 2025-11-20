
user_input = int(input("enter a five digit integer: "))
for digit in range(5):
    denominator = 10
    separated = user_input % 10
    user_input //= 10
    print(separated, end='')
print()
    
