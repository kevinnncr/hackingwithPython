def count_words(text):
    words = text.split()
    number_of_words = len(words)
    return number_of_words

filename = 'words.txt'

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

number_of_words = count_words(text)
print(f" {number_of_words}")
