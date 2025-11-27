def discount_checker(name_of_item,original_price,promotional_code):
    if(promotional_code == 'SAVE10'):
    
        discount = original_price-(original_price * 0.1)
        return discount
    elif(promotional_code == 'HALFOFF'):
        discount = original_price-(original_price * 0.5)
        return discount
    elif(promotional_code != 'HALFOFF' | promotional_code == "SAVE10"):
        return str(discount) + "Invalid promotional code" 
    else:
        return discount

print(discount_checker(27,12,"HALFOFF"))
