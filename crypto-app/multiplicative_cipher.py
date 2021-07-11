def multi_encrypt(input_text, key=4):
    output = ""
    for i in range(len(input_text)):
        temp = input_text[i]
        output += chr(ord(temp)*key)
    return output

def multi_decrypt(input_text, key=4):
    output = ""
    for i in range(len(input_text)):
        temp = input_text[i]
        output += chr(ord(temp)//key)
    return output
