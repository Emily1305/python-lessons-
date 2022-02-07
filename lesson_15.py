# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:06:30 2022

Working with dictionaries 
"""

# student = {
#     'name': 'Beth', 
#     'surname': 'Harmon', 
#     'age': 20, 
#     'major': 'computer science', 
#     'title': 'senior'
#     }
# print(student.items())
# for key, value in student.items():
#     print(f"Key: {key}")
#     print(f"Value: {value}\n")


# fruits = {
#     'apple': 3,
#     'orange': 5,
#     'banana': 2,
#     'grapes': 6
#     }
# print('The following are fruits:')
# for item in fruits.keys():
#     print(item)

# python = {
#     'string': 'matn', 
#     'integer': 'butun son',
#     'float': 'kasr son', 
#     'if': 'agar', 
#     'else': 'aks holda', 
#     'list': "ro'yxat",
#     'tuple': "o'zgarmas ro'yxat", 
#     'set': "elementlari takrorlanmaydigan lug'at"
    
#     }

# for key, value in sorted(python.items()):
#     print(key+ ' - ' + value)

countries = {
    'Uzbekistan': 'Tashkent', 
    'USA': 'Washington', 
    'Turkey': 'Ankara', 
    'India': 'Dehli'
    }

# for country in sorted(countries.keys()):
#     print(country)

# for capitals in sorted(countries.values()):
#     print(capitals)

# user = input('Enter the name of country: ').title()
# capital = countries.get(user)
# if capital == None:
#     print(f"{user} does not exist in the list")
# else:
#     print(f"The capital of {user} is {capital}")