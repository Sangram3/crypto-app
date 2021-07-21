def case_transform(input_text):
    output_text = ''
    for letter in input_text:
        if 65 <= ord(letter) and ord(letter) <= 90:
            output_text += chr(ord(letter) + 32)
        elif 97 <= ord(letter) and ord(letter) <= 122:
            output_text += chr(ord(letter) - 32)
        else:
            output_text += letter
    return output_text

#print(case_transform('InDiA'))
