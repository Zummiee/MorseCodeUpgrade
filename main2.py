''' This project enables user to input a string and then turns the string into its Morse Code equivalent, have fun!!'''

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': ' / ', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'}


def Morse_Code_Converter():
    input_word = input("input a string: ")
    word_elements = list(input_word.upper())
    converted_elements = []
    game_on = True
    for element in word_elements:
        if not element in morse_code_dict:
            print(f"{element} does not exist in Morse Code, please input another string")
            game_on = False
            Morse_Code_Converter()
            break
        else:
            element_converted = morse_code_dict[element]
            converted_elements.append(element_converted)
    if game_on:
        converted_word = ' '.join(converted_elements)
        print(f"the string '{input_word}' converted to Morse Code would be '{converted_word}'")
        continue_game()


def continue_game():
    to_continue = input("\nwould you like to convert another string? (input 'y' for 'yes' and 'n' for 'no': ")
    if to_continue == "y":
        Morse_Code_Converter()
    elif to_continue == "n":
        print("I am sorry to see you go, hope you had fun converting!")
    else:
        print("Sorry, I am not sure what you mean, please try again")
        continue_game()


Morse_Code_Converter()
