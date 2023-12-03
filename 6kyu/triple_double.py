#https://www.codewars.com/kata/55d5434f269c0c3f1b000058/train/python
def triple_double(num1, num2):
    num1 = str(num1)
    num2 = str(num2)

    for i in range(len(num1) - 2):
        if num1[i] == num1[i + 1] == num1[i + 2]:
            for j in range(len(num2) - 1):
                if num2[j] == num2[j + 1] == num1[i]:
                    return 1
    return 0
triple_double(451999277, 41177722899)
# triple_double(1222345, 12345)
# triple_double(12345, 12345)
# triple_double(666789, 12345667)