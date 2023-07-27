def extract_uppercase(text):
    words = text.split()
    uppercase = [word for word in words if word.isupper()]
    filtered_uppercase = []
    for word in uppercase:
        filtered_letters = [letter for letter in word if letter.isalpha()]
        filtered_word = "".join(filtered_letters)
        filtered_uppercase.append(filtered_word)
    return filtered_uppercase
