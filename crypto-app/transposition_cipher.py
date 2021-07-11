

def transposition_encrypt( input_text , key ):
    """ NOTE : if entered key has repeated characters key is change to UNIQUE """

    se = set()
    for i in key:
        se.add(i)
    if len(se )!= len(key):
        key = ''

    if key == '':
        key = 'UNIQUE'
    
    key_len = len(key)
    output_text = ""
    store = [ [ [key[row]] , [] ]for row in range(key_len)]
    index= 0
    for letter in input_text:
        pos = index % key_len
        store[pos][1].append(letter)
        index += 1
    store.sort()

    for i in store:
        for j in i[1]:
            output_text+= j
    return output_text

def transposition_decrypt( input_text , key):
    """ NOTE : if entered key has repeated characters key is change to UNIQUE """
    N = len(input_text)
    se = set()
    for i in key:
        se.add(i)

    if len(se )!= len(key):
        key = ''

    if key == '':
        key = 'UNIQUE'

    key_len = len(key)
    output_text = ""
    store = {}

    copy = []
    cnt = {}
    for i in key:
        cnt.update({i:0})
        store.update({i : []})
        copy .append(i)
    copy.sort()
    for i in range(N):
        cnt[key[i%key_len] ] +=1

    index = 0
    j = 0
    while index < N:
        for i in range(index  , index + cnt[copy[j]]):
            store[copy[j]].append(input_text[i])
        index+=cnt[copy[j]]
        j+=1
  
    index = 0
    while True:
        flag = 0
        for i in key:
            if len(store[i] )> index:
                flag = 1
                output_text+= store[i][index]
        if flag == 0:
            break
        index+=1
    return output_text

 
# print(transposition_decrypt(transposition_encrypt("{Alex} ,{Hales}" , "HACK") , "HACK") )

