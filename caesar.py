import string
from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted = encrypted + ' '
        elif char in alphabet:
            rotated_index = rotate_character(char,rot)
            
            encrypted = encrypted + rotated_index
            
            
        elif char in alphabet1:
            rotated_index = rotate_character(char,rot)   
            
            
            encrypted = encrypted + rotated_index
        
                
        else:
            encrypted = encrypted + char
        
    return encrypted

def main():
    mes = input("Type a message: ")
    rot1 = int(input("Rotate by: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(rotate_string(mes, rot1))
    print(alphabet_position(mes))
    print(encrypt(mes, rot1))

if __name__ == "__main__":
    main()