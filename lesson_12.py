# -*- coding: utf-8 -*-
"""
February 6, Type of errors
"""

number = float(input("Enter even number: "))
if number % 2 != 0:
    print("This number is not even")
else:
    print("Thank you")


age = int(input("How old are you?"))
if age<=4 or age>=60:
    cost = 0
elif age < 18:
    cost = 10000
else:
    cost = 20000
print(f"Tickets costs {cost} sums")


x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")


products = ['flour', "oil", "soap", 'egg', 'onion',
                'potato', 'apple', 'banana', 'grapes', 'melon']
basket = [] 
for n in range(5):
    basket.append(input(f"Add {n+1}-product to your basket:  "))

if basket:
    for product in basket:
        if product in products:
            print(f"We have {product} in our shop")
        else:
            print(f"We do not have {product} in our shop")
else: 
    print("Your basket is empty ") 






products = ['flour', "oil", "soap", 'egg', 'onion',
                'potato', 'apple', 'banana', 'grapes', 'melon']
basket = []
for n in range(5):
    basket.append(input(f"Add {n+1}-product to your basket:  "))

existing_products = []
non_existing_products = []
for product in basket:
    if product in products:
        existing_products.append(product)
    else:
        non_existing_products.append(product)

if non_existing_products:
  print("We do not have these products:")
for product in non_existing_products:
  print(product)
else:
  print("We have everything you asked ")
    


