# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 15:12:48 2023

@author: DELL
"""

# yosh = int(input("Yoshingiz nechida: "))

# if yosh <= 4:
#     narh = 0
# elif yosh <= 12:
#     narh = 5000
# elif yosh <= 18:
#     narh = 8000
# else:
#     narh = 10000
    
# print("Sizga kirish tekin") if narh == 0 else print(f"Sizga kirish {narh} so'm")



# kun = input("Bugun nima kun? \n>>> ")

# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba' :
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")



# day = input("Bugun qaysi kun? \n>>> ")
# harorat = float(input("Harorat necha daraja? \n>>> "))

# if day.lower() == 'yakshanba' and harorat >= 30:
#     print("Ketdik cho'milishga")
# elif day.lower() == 'yakshanba' and harorat < 30:
#     print("Uyda dam olamiz")
    
# if (day.lower() == 'shanba' or day.lower() == 'yakshanba') and harorat >= 30:
#     print("Kettu cho'milgani")
# elif (day.lower() == 'shanba' or day.lower()== 'yakshanba') and harorat < 30:
#     print("Uyda dam olilu")



# narh = 15000
# choy = True
# salat = False

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
    
# print(f"Jami {narh} so'm")
    


# narh = 15000
# choy = True
# salat = False
# non = 1
# kompot = 0
# assorti = 1

# if choy:
#     print("Mijoz choy oldi")
#     narh = narh + 3000
    
# if salat:
#     print("Mijoz salat oldi")
#     narh = narh + 5000
    
# if non:
#     print("Mijoz non oldi")
#     narh = narh + 4000
    
# if kompot:
#     print("MIjoz kompot oldi")
#     narh = narh + 6000
    
# if assorti:
#     print('Mijoz assorti sotib oldi')
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm bo'ldi")



# menu = ['osh', 'qozonkabob', 'norin', 'somsa', 'shashlik']

# bool_f = 'manti' in menu  # False
# bool_t = 'somsa' in menu  # True

# ovqat = input("Nima ovqat yeysiz? \n")

# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday taom yo'q")
    
# if ovqat.lower() not in menu:
#     print("Afsuski bizda bunday taom yo'q")
# else:
#     print("Buyurtma qabul qilindi")
        


# menu = ['osh', 'qozonkabob', 'norin', 'somsa', 'shashlik']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# if buyurtmalar:  # Ro'yhatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz menuda {taom} yo'q")
# else:   # buyurtmalar ro'yhati bo'sh bo'lsa FALSE qaytaradi
#     print("Savatchangiz bo'sh ekan")

########################## AMALIYOT ####################################

# son = int(input("Juft son kiriting: "))

# if son%2 :
#     print("Bu son juft emas")
# else:
#     print("Rahmat!")



# yosh = int(input("Yoshingiz nechchida? "))

# if yosh <= 4 or yosh >=60 :
#     narh = 0
# elif yosh <= 18:
#     narh = 10000
# else:
#     narh = 20000
  
# print("Sizga chipta tekin") if narh == 0 else print(f"Chipta narhi {narh} so'm")




# a = float(input("Birinchi sonni kiritng: "))
# b = float(input("Ikkinchi sonni kiritng: "))

# if a > b:
#     print(f"{a} > {b}")
# elif a == b:
#     print(f"{a} = {b}")
# else:
#     print(f"{a} < {b}")




# mahsulotlar = ['uzum', 'olma','anjir', 'nok', 'behi', 'o\'rik', 'gilos', 'qovun', 'shaftoli', 'olxo\'ri']
# savat = []

# for i in range(5):
#     savat.append(input(f"Savatga {i+1}-mahsulotni qo'shing: "))

# print("")

# for m in savat:
#     if m.lower() in mahsulotlar:
#         print(f"Do'konimizda {m.title()} bor")
#     else:
#         print(f"Do'konimizda {m.title()} yo'q")
        
    
    

# mahsulotlar = ['uzum', 'olma','anjir', 'nok', 'behi', 'o\'rik', 'gilos', 'qovun', 'shaftoli', 'olxo\'ri']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []

# for i in range(5):
#     savat.append(input(f"Savatga {i+1}-mahsulotni qo'shing: "))

# print("")

# for m in savat:
#     if m.lower() in mahsulotlar:
#         bor_mahsulotlar.append(m)
#     else:
#         mavjud_emas.append(m)
        
# if mavjud_emas:
#     print("Quyidagi mahsulotlar do'konimizda yo'q: ")
#     for n in mavjud_emas:
#         print(n)
# else:
#     print( "Siz so'ragan barcha mahsulotlar do'konimizda bor" )
    
# print("bor_maxsulotlar -",bor_mahsulotlar)
# print("mavjud_emas -",mavjud_emas)




# foydalanuvchilar = ['Alibek', 'Cristiano', 'Asomiddin', 'Jamshid', 'Merlin']

# if (input("Yangi login tanlang: ")).title() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz, foydalanuvchi!")




a = int(input("Istalgan butun son kiriting: "))

for i in range(2,11):
    # if a%i == 0:
    if not (a%i):
        print(f"{a} soni {i} ga qoldiqsiz bo'linadi")

print("GitHub ga yuklandi")