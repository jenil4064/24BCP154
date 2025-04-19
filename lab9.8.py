def convert(text):
    words = text.split()
    unique_words = set(words)
    sorted_words = sorted(list(unique_words))
    result = ' '.join(sorted_words)
    return result

input_text = "apple banana apple orange banana mango"
output_text = convert(input_text)
print("Result after removing duplicates and sorting:", output_text)