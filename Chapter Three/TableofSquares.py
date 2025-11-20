print("number\tsquare\tcube")
for number in range(0,6):
    number_square = (number ** 2)
    number_cube = (number ** 3)
    print(f"{number:>4}\t {number_square:>4}\t{number_cube:>4}")
