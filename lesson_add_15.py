# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 03:10:24 2022
Working with dictionaries 
"""

'''
Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
'''
python = {
    'integer': 'butun son', 
    'float': 'kasr son',
    'string' : 'matn', 
    'list' : "ro'yxat",
    'tuple' : "o'zgarmas ro'yxat",
    'if' : 'agar',
    'else' : 'aks holda',
    'variable' : "o'zgaruvchi",
    'set' : "elementlari takrorlanmaydigan ro'yxat"
    }

for key, value in python.items():
    print(f"{key} - {value}")





'''
Davlatlar va ularning poytaxtlari lug'atini tuzing. 
Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
'''
countries = {
    'uzbekistan' : 'tashkent',
    'russia' : 'moscow', 
    'usa' : 'washington',
    'kyrgyzistan' : 'bishkek',
    'tajikistan' : 'dushanbe', 
    'china' : 'pekin'
    }

for keys in sorted(countries.keys()):
    print(keys.title())
for values in sorted(countries.values()):
    print(values.title())
'''
Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
'''    
user = input("Davlat nomini kiriting: ").lower()
capital = countries.get(user)
if capital == None:
    print("Bizda bunday ma'lumot yo'q")
else:
    print(f"The capital of {user.title()} is {capital.title()}")






'''
Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, 
aks holda "bizda bunday taom yo'q" degan xabarni chiqaring
'''
menu = {
        'osh' : 20000,
        'manti' : 5000,
        'chuchvara' : 12000,
        "lag'mon" : 18000,
        'somsa' : 4000
        }
zakazlar = []
print("3 ta taom buyurtma bering")
for n in range(3):
    zakazlar.append(input(f"{n+1} - taom: ").lower())
for zakaz in zakazlar:
    if zakaz in menu:
        print(f"{zakaz.title()} {menu[zakaz]} so'm")
    else:
        print("Bizda bunday taom yo'q")