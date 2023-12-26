# https://www.codewars.com/kata/57fb142297e0860073000064/train/python
def product(st):
    return st.count("!") * st.count("?")


print(product('!!??!!'))