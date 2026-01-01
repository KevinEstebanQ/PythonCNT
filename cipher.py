#letter = "a"
## converts a letter to ascii code 
#ascii_code = ord(letter) 
## converts ascii code to a letter 
#letter_res = chr(ascii_code) 
#print (ascii_code, letter_res) 97, a
#ascii_code+=3
#print(chr(ascii_code)) d

def cesar_cipher(text, shift):
    encoded_text=""
    for letter in text:
        if letter.isalpha():

            if ord(letter)>=65 and ord(letter)<=90:

                shiftedletter = (ord(letter)-65+shift)%26 + 65
                shiftedletter = chr(shiftedletter)
                encoded_text+=shiftedletter

            elif ord(letter)>=97 and ord(letter)<=122:
                 
                 shiftedletter = (ord(letter)-97+shift)%26 + 97
                 shiftedletter = chr(shiftedletter)
                 encoded_text+=shiftedletter
        else:
            encoded_text+=letter
    return encoded_text

text = input("text to encrypt: ")
shift = int(input("shift amount: "))
print(cesar_cipher(text, shift))
