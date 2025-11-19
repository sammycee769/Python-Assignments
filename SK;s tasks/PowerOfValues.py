counter = 1
print("a\tb\tpow(a,b)")
while(counter <= 5):
    counter_add = counter + 1
    counter_expo = counter ** (counter + 1)
    print(f"{counter}\t{counter_add}\t{counter_expo}")
    counter += 1
