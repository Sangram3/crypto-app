def case_transform(input_text):
    output_text = ''
    for letter in input_text:
        if ord(letter) <= 90:
            output_text += chr(ord(letter) + 32)
        else:
            output_text += chr(ord(letter) - 32)
    return output_text

# print(case_transform('InDiA'))