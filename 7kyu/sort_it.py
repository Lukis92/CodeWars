#https://www.codewars.com/kata/54eea36b7f914221eb000e2f/train/python
def sort_it(words, n):
    words = words.split(", ")
    sorted_words = sorted(words, key=lambda x: x[n-1])
    return ", ".join(sorted_words)
    print(sorted_words)
    #return sorted(words, key=lambda x: list(words.split(", "))[n-1])
    #print(list(words.split(", ")))


print(sort_it('bill, bell, ball, bull', 2)) #,'ball, bell, bill, bull'