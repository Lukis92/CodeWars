# https://www.codewars.com/kata/57faf32df815ebd49e000117/train/python
def remove(st):
    modified_words = []

    for word in st.split():
        while word.endswith('!'):
            word = word[:-1]

        modified_words.append(word)

    return " ".join(modified_words)

print(remove("Hi!"))