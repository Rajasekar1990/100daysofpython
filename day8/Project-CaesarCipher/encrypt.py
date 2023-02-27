alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_fn (text_to_encode,shift_front):
    encoded_text=""
    for i in text_to_encode:
        curr_pos = alphabet.index(i)
        new_pos =  curr_pos + shift_front
        new_i = alphabet[new_pos]
        encoded_text += new_i
    print(f"encoded text is: {encoded_text}")