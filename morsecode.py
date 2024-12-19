# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher


def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    space_count = 0 
    
    for letter in message:
        if letter != ' ':
            space_count = 0 
            citext += letter
        else:
            space_count += 1
            if space_count == 2:
                decipher += ' '
            elif citext:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
                
    return decipher



def encryptor():
    message = input("Put your message here to convert it to Morsecode.\n")
    result = encrypt(message.upper())
    print(result)


def decryptor():
    message = input("Put your morse code here to convert it to Text.\n")
    result = decrypt(message)
    print(result)


def main():

    opt = input(
        "• Press 1 to translate Text to Morse code. \n• Press 2 to translate Morse code to Text.\nType here: ")
    opt = int(opt)

    if (opt == 1):
        encryptor()
    elif (opt == 2):
        decryptor()
    else:
        print("Please choose a valid input.")
main()
