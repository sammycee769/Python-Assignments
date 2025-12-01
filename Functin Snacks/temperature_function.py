def temp_checker(number,temperature_unit,threshold):
    if type(number) is str or type(threshold) is str:
        raise TypeError("Input a ")
    if type(temperature_unit) is not str: 
        raise TypeError("Input must be string")
    if temperature_unit not in ("C","F","c","f"):
        raise TypeError("Temperature must be C or F")
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
    
#print(temp_checker(90,"g",19))
