def length_of_word(word):
    digit = 0
    for count in word:
        digit+=1
    return digit
   
def reverse(word):
    reverse = " "
    for letter in word:
        reverse = letter + reverse
    return reverse
def get_hours (minutes):
    hours = minutes / 60
    seconds_remaining = minutes * 60
    return f"{minutes}min in sec is {seconds_remaining} and in hour is {hours}"
def vowels_in_word (word):
    vowels = "aeiou"

    count = 0
    for letter in vowels:
        if word.count(letter) >= 1 :
            count += 1

    return count  

print(vowels_in_word("pineapple"))
