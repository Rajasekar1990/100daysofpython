def caesar_fn(text_fn,shift_fn,direction_fn):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        final_word=""

        if(direction_fn == "decode"):
            shift_fn*=(-1)

        for i in text_fn:
            if (i not in alphabet):
                final_word+=i
            else:
                current_pos=alphabet.index(i)
                # if (direction_fn == "decode"):
                #     new_pos = current_pos - shift_fn
                # elif (direction_fn == "encode"):
                #     new_pos = current_pos + shift_fn
                new_pos = current_pos + shift_fn
                new_i = alphabet[new_pos]
                final_word+=new_i
        
        print(f"encoded text is: {final_word}")