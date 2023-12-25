# https://www.codewars.com/kata/552564a82142d701f5001228/train/python
def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / (1 - sale_percentage/100), 2)

print(discover_original_price(75,25)) #100