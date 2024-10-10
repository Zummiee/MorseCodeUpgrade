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
    for element in word_elements:
        if not element in morse_code_dict:
            print("string contains element that does not exist in Morse Code, please input a new string")
            Morse_Code_Converter()
    converted_elements = []
    for element in word_elements:
        element_converted = morse_code_dict[element]
        converted_elements.append(element_converted)
    converted_word = ' '.join(converted_elements)

    print(f"the string '{input_word}' converted to Morse Code would be '{converted_word}'")
    game_on = True
    while game_on:
        continue_game = input("\nwould you like to convert another string? (input 'y' for 'yes' and 'n' for 'no': ")
        if continue_game == "y":
            Morse_Code_Converter()
            game_on = False
        elif continue_game == "n":
            print("I am sorry to see you go, hope you had fun converting!")
            game_on = False
        else:
            print("Sorry, I am not sure what you mean, please try again")

Morse_Code_Converter()
