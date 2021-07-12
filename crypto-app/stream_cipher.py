# import sys,os,io
def bin32(num):
    return '{0:010b}'.format(num)

def stream_encrypt(input_text , key):
    se = set()

    copy = ''
    N = len(key)
    for i in range(10):
        copy += key[(i%N)]

    key = copy
    for letter in input_text:
        if letter != ' ':
            se.add(letter)
    code = {}
    for i in se:

        b = bin32(ord(i))
        
        x = ''
        for j in range(10):
            x += str(int(key[j]) ^ int(b[j]) )
        code[i] = x
    
    output_text = ''
    for letter in input_text:
        if letter  == ' ':
            output_text += ' '
            continue
        output_text += code[letter]
    
    return output_text

def stream_decrypt( input_text , key):
    copy = ''
    N = len(key)
    for i in range(10):
        copy += key[(i%N)]
    key = []
    for i in copy:
        key.append(int(i))

    N = len(input_text)
    ind = 0
    output_text = ''
    while ind  < N:
        if input_text[ind] == ' ':
            output_text+=' '
            ind+=1
            continue
        x = []
        for i in range(ind , ind + 10):
            x.append(int(input_text[i]))
        ans = []
        for i in range(10):
            ans.append(x[i] ^ key[i])
        
        ans.reverse()
        final = 0
        total = 1
        for i in range(10):
            final += ans[i] * total
            total *=2
        output_text += chr(final)
        ind +=10
    return output_text

# print(stream_decrypt(stream_encrypt('{Alex},{Hales}' , '10001') , '10001'))


