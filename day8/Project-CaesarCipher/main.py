from img import logo
#print(logo)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

from encrypt import encrypt_fn
from decrypt import decrypt_fn
from caeser import caesar_fn

repeatcheckflag = True
while repeatcheckflag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if (shift > 26):
        shift%=26
        print(f"shift value is: {shift}")

    # if (direction == "encode"):
    #     encrypt_fn(text_to_encode=text, shift_front=shift) 
    # elif (direction == "decode"):
    #     decrypt_fn(text_to_decode=text, shift_back=shift)

    caesar_fn(text_fn=text, shift_fn=shift, direction_fn=direction)
    repeatcheck = input("Type YES if you want to continue and incase not type NO \n").lower()

    if repeatcheck != "yes":
        repeatcheckflag = False


#method 2 for handling shift number 
# pos = alphabet.index("z")
# shift = int(input("Type the shift number:\n"))
# actualshift=pos+shift
# print(actualshift)
# if (actualshift > 26):
#     actualshift%=26
# else:
#     actualshift=pos+shift
# print(f"shift value is: {actualshift}")
# print(f"givenchar: {alphabet.index('z')} decoded char: {alphabet[actualshift]}")