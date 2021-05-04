def cap_even_letters(string):
    new_string=""
    for letter_index in range(len(string)):
        if letter_index%2 == 0:
            new_string += string[letter_index].upper()
        else:
            new_string += string[letter_index]
    return(new_string)

string = input("Type senctence to be sickafied: ")
print("Sickafied sentence: " + cap_even_letters(f"{string}"))
