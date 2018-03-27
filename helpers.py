import string
def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    
    for i in letter:
        if i in string.ascii_lowercase:
            index = alphabet.index(i)
        else:
            if i in string.ascii_uppercase:
                index = alphabet1.index(i) 
        
    return(index)

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    rot_char = ""
    for i in char:
        if i in alphabet:
            rotated_index = alphabet_position(i) + rot
            if rotated_index < 26:
                rot_char = alphabet[rotated_index]
            else:
                rot_char = alphabet[rotated_index % 26]
        else:
            if i in alphabet1:
                rotated_index = alphabet_position(i) + rot
            if rotated_index < 26:
                rot_char = alphabet1[rotated_index]
            else:
                rot_char = alphabet1[rotated_index % 26]
    return rot_char