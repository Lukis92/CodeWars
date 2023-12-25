# https://www.codewars.com/kata/57212c55b6fa235edc0002a2/train/python
def common_ground(s1,s2):
    words_s1 = set(s1.split())
    words_s2 = s2.split()

    common_words = [word for word in words_s2 if word in words_s1]
    
    if not common_words:
        return "death"
    
    seen = set()
    result = []
    for word in common_words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return " ".join(result)


print(common_ground("eat chicken", "eat chicken and rice"))