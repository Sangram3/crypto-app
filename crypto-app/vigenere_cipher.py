
# Transposition cipher
# Affine cipher
# vigenere cipher

def vigenere_encrypt( input_text , key ):
    if key == '':
        key = 'vigenere_cipher'

    output_text = ""
    key_len = len(key)
    index = 0
    for letter in input_text:
        if letter == ' ':
            output_text+= ' '
            continue
        pos = index % key_len
        ordi = ord(letter) + ord(key[pos])
        output_text += chr(ordi)
        index+=1
    return output_text

def vigenere_decrypt(input_text , key):
    if key == '':
        key = 'vigenere_cipher'
    output_text = ""

    key_len = len(key)
    index= 0
    for letter in input_text:
        if letter == ' ':
            output_text+= ' '
            continue
        pos = index % key_len
        ordi =  ord(letter) - ord(key[pos])
        output_text+= chr(ordi)
        index+=1
    return output_text
    
# print( vigenere_decrypt ( vigenere_encrypt('Dansflh DIFHJKSHF ' , 'zebra') ,'zebra') )

