def caesar_encryption(inp_text, shift):
    shift = shift % 10000
    output = ""
    for i in range(len(inp_text)):
        temp = inp_text[i]
        output += chr(ord(temp) + shift)
    return output

def caesar_decryption(inp_text, shift):
    shift = shift % 10000
    output = ""
    for i in range(len(inp_text)):
        temp = inp_text[i]
        output += chr(ord(temp) - shift)
    return output
