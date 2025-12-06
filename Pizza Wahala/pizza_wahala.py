sapa_slice = 4
sapa_price = 2000
small_money_slice = 6
small_money_price = 2400
big_boys_slice = 8
big_boys_price = 3000
odogwu_slice = 12
odogwu_price = 4200

print("""--------Menu-------
Sapa size
Sapa_slice = 4
Sapa_price = 2000

Small Money size
Small_money_slice = 6
Small_money_price = 2400

Big Boys size
Big_boys_slice = 8
Big_boys_price = 3000

Odogwu size
Odogwu_slice = 12
Odogwu_price = 4200
 """)
number_of_people = int(input("How Many Guests Do You Intend Serving: "))
pizza_type = input("What Type Of Pizza Do You Intend Buying: ").lower()

if pizza_type not in ["small money size","sapa size","big boys size","odogwu size" ]  or number_of_people <= 0:
    print("invalid Selection")
    exit()

if pizza_type == "sapa size" and number_of_people % sapa_slice == 0:
    pizza_box =  number_of_people / sapa_slice
    amount_to_pay = sapa_price * pizza_box
    leftover = 0
elif pizza_type == "sapa size" and number_of_people % sapa_slice != 0:
    pizza_box =  (number_of_people // sapa_slice) + 1
    amount_to_pay = sapa_price * pizza_box
    leftover = (pizza_box * sapa_slice) - number_of_people

if pizza_type == "small money size" and number_of_people % small_money_slice == 0:
    pizza_box =  number_of_people / small_money_slice
    amount_to_pay = small_money_price * pizza_box
    leftover = 0
elif pizza_type == "ssmall money size" and number_of_people % small_money_slice != 0:
    pizza_box =  (number_of_people // small_money_slice) + 1
    amount_to_pay = small_money_price * pizza_box
    leftover = (pizza_box * small_money_slice) - number_of_people

if pizza_type == "big boys size" and number_of_people % big_boys_slice == 0:
    pizza_box =  number_of_people / big_boys_slice
    amount_to_pay = big_boys_price * pizza_box
    leftover = 0
elif pizza_type == "big boys size" and number_of_people % big_boys_slice != 0:
    pizza_box =  (number_of_people // big_boys_slice) + 1
    amount_to_pay = big_boys_price * pizza_box
    leftover = (pizza_box * big_boys_slice) - number_of_people

if pizza_type == "odogwu size" and number_of_people % odogwu_slice == 0:
    pizza_box =  number_of_people / odogwu_slice
    amount_to_pay = odogwu_price * pizza_box
    leftover = 0
elif pizza_type == "odogwu size" and number_of_people % odogwu_slice != 0:
    pizza_box =  (number_of_people // odogwu_slice) + 1
    amount_to_pay = odogwu_price * pizza_box
    leftover = (pizza_box * odogwu_slice) - number_of_people

print("Number of boxes of pizza to buy = ",int(pizza_box), "boxes") 
print("Number of left over slice after serving = ",leftover, "slices")
print("Amount= ", amount_to_pay)

