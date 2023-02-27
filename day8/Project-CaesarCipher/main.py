from img import logo
print(logo)

# from encrypt import encrypt_fn
# from decrypt import decrypt_fn
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