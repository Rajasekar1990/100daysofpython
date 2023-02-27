alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt_fn (text_to_decode , shift_back):
    decoded_text=""
    for j in text_to_decode:
        curr_pos = alphabet.index(j)
        new_pos =  curr_pos - shift_back
        new_j = alphabet[new_pos]
        decoded_text += new_j
    print(f"encoded text is: {decoded_text}")