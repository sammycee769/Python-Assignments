letter = input("Enter a letter: ").lower()

if(letter.isdigit()):
    print("invalid input")
elif letter in ("a", "e", "i", "o", "u"):
    print("Vowel")
else:print("consonant")
