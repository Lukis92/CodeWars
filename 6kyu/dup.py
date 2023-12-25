#https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python
def dup(arry):
    result = []
    for word in arry:
        new_word = ""
        for i in range(len(word)):
            if i == 0 or word[i] != word[i-1]:
                new_word += word[i]
        result.append(new_word)
    return result

dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"])