# https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/python
def reverse_number(n):
    print("".join(reversed([d for d in str(n)])))
    return reversed([n])

print(reverse_number(123))#, 321)
print(reverse_number(-123))#, -321)#, 'Negative Numbers should be preserved')
print(reverse_number(1000))#, 1)
print(reverse_number(4321234))#, 4321234)
print(reverse_number(5))#, 5)
print(reverse_number(0))#, 0)
print(reverse_number(98989898))#, 89898989)
