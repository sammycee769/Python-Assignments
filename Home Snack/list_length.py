def check_last_first_index(*words):
    new_word = []
    count = 0
    for string in words:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
            new_word.append(string)
    return count,new_word
                

    



print(check_last_first_index("samuel", "ayobama", "amela", " smas"))
