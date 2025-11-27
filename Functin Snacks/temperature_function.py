def temp_checker(number,temperature_unit,threshold):
    if(temperature_unit == 'C' or temperature_unit == 'c'):
        temperature_unit_in_fahrenheit = (number * (9/5))+32
        threshold_in_fahrenheit = (threshold * (9/5))+32
        if(temperature_unit_in_fahrenheit >= threshold_in_fahrenheit):
            return"Heat alert"
        else:
            "Cold advisory"
    elif(temperature_unit == 'F' or temperature_unit == 'f'):
        threshold_in_celsius = (number - 32)*(5/9)
        temperature_unit_in_celsius = (number - 32)*(5/9)
        if(temperature_unit_in_celsius >= threshold_in_celsius):
            return"Heat alert"
        else:
            "Cold advisory"
    else:
        return "Invalid Input"
    
#print(temp_checker(27,"c",19))
