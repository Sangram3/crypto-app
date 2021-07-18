def reverse(input_text):
    input_text = list(input_text)
    input_text.reverse()
    output_text = "".join(input_text)
    return output_text

# print(reverse("India"))