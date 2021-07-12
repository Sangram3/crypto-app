def autokey_encrypt(input_text, key):
    output = ""
    key = key + input_text
    for i in range(len(input_text)):
        output += chr(ord(input_text[i]) + ord(key[i]))
    return output

def autokey_decrypt(input_text, key):
    output = ""
    for i in range(len(input_text)):
        temp = chr(ord(input_text[i]) - ord(key[i]))
        output += temp
        key += temp
    return output
        


text = "hello my friends"
key = "hhe"
print("Text: " + text)
print("Key: " + key)
print("Encrypt: " + autokey_encrypt(text, key))
print("Decrypt: " + autokey_decrypt(autokey_encrypt(text, key), key))