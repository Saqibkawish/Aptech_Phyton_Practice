# #
# # applicant_name = input("Enter Applicant Name : ")
# # job_applied_for = input("Enter job applied for : ")
# # expected_salary = int(input("Enter expected salary : "))
# # available_for_interview = input("Available for interview  : ")
# #
# # print("Application Name :" , applicant_name , " job_applied_for" , job_applied_for , "Expected_salary" , expected_salary , "Available For Interview" , available_for_interview)
# #
# # print(f"Applicant Name is {applicant_name} \n job applied for {job_applied_for} \n expected_salary {expected_salary} \n available for interview {available_for_interview}")
#
#
# print("MY Halwa Pori Shoq")
# no_of_pori = int(input("How Many Pori do you want...?"))
# no_of_choly_plates = int(input("HOW many choly plates Do you want...?"))
# no_of_Alu_tarkari_plates = int(input("HOW many alu tarkari plates Do you want...?"))
# no_of_halwa_plates= int(input("How Many Halwa plates do you want...?"))
#
# per_pori = 50
# per_choly_plate = 80
# per_alu_plates = 70
# per_halwa_plates = 100
#
# pori_total = no_of_pori * per_pori
# choly_plate_total = no_of_choly_plates * per_choly_plate
# alu_plates_total = no_of_Alu_tarkari_plates * per_alu_plates
# halwa_totals = no_of_halwa_plates * per_halwa_plates
#
# Total_bill = pori_total + choly_plate_total + alu_plates_total + halwa_totals
#
# payment_method = input("Do You want to PAy with card....? yes / no ")
#
# if payment_method == "yes" :
#     tax = Total_bill * 0.08
# else :
#     tax = 0
#
# final_bill = Total_bill + tax
#
# discount = final_bill * 0.25
#
# bill_after_discount = final_bill - discount
#
# print(bill_after_discount)
#
# print(f"No of pori : {no_of_pori} \n No of Choly PLates : {no_of_choly_plates} \n No of Alu plates : {no_of_Alu_tarkari_plates} \n No of Halwa Plates {no_of_halwa_plates} \n Your Total Bill is { Total_bill} \n tax : {tax} \n Your Final Bill is {final_bill} \n Discount : {discount} \n Bill After Discount : {bill_after_discount}")
#
from operator import truediv

# import random

# Generates a random float between 0.0 and 1.0
# a = random.random()
# print(a)

# Generates a random integer between 2 and 6
# int_random = random.randint(2, 6)
# print(int_random)

# List of student names
# stu_names = ["Zain", "Ali", "Arham", "Frhan", "Arslan"]

# Randomly choose one name
# print(random.choice(stu_names))

# Shuffle the list in place
# random.shuffle(stu_names)
# print(stu_names)  # You must use print, not random()

# Get a random sample of 2 names from the list
# samp = random.sample(stu_names, k=2)
# print(samp)


# import random
#
# print("------------ Number Guessing Game ------------")
# computer_ka_no = random.randint(1, 20)
# lives = 3
#
# while lives > 0:
#     user_guess = int(input("Enter Your Guess between 1 - 20: "))
#
#     if user_guess == computer_ka_no:
#         print("Congratulations You've Guessed")
#         break
#     else:
#         lives -= 1
#
#         if user_guess > computer_ka_no:
#             print("Please Guess Low Number")
#         else:
#             print("Please Guess High Number")
#
#         if lives > 0:
#             print(f"You've {lives} lives remaining")
#         else:
#             print("All Lives has been Finished")


     # random password generator
# import random
# import string
# import sys
#
# import pyperclip
#
# print("********** Random Password Generator **********\n")
#
# uppercase_length = int(input("How many Upper Letters Do you want? "))
# if uppercase_length <= 0 or uppercase_length > 10 :
#     print("At least 1 uppercase is required and maximum 10 ")
#     sys.exit()
# lowercase_length = int(input("How many Lower Letters Do you want? "))
# if lowercase_length <= 0 or uppercase_length > 10 :
#     print("At least 1 Lowercase is required and maximum 10 ")
#     sys.exit()
# digit_length = int(input("How many Numbers Do you want? "))
# if digit_length <= 0 or uppercase_length > 10 :
#     print("At least 1 Digit length  is required and maximum 10 ")
#     sys.exit()
# special_character_length = int(input("How many Special Characters Do you want? "))
# if special_character_length <= 0 or uppercase_length > 10 :
#     print("At least 1 special character length is required and maximum 10 ")
#     sys.exit()
#
# uppercase = string.ascii_uppercase
# lowercase = string.ascii_lowercase
# numbers = string.digits
# special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
#
# upper_list, lower_list, number_list, sp_list = [], [], [], []
#
# for i in range(uppercase_length):
#     upper_list.append(random.choice(uppercase))
#
# for i in range(lowercase_length):
#     lower_list.append(random.choice(lowercase))
#
# for i in range(digit_length):
#     number_list.append(random.choice(numbers))
#
# for i in range(special_character_length):
#     sp_list.append(random.choice(special_characters))
#
# PasswordList = upper_list + lower_list + sp_list + number_list
# random.shuffle(PasswordList)
#
# pswd_string = "".join(PasswordList)
# print("\nYour Generated Password is:", pswd_string)
#
#
# choice = input("Do you want to copy this password? (yes/no): ")
# if choice.lower() == "yes":
#     pyperclip.copy(pswd_string)
#     print("Password has been copied to clipboard.")

# user_salary = int(input("Enter Your salary "))
# print('Expenses')
#
# user_home = input("do You live in your own house...?  yes/no ")
#
# if user_home.lower() == "no" :
#     user_rent = int(input("Enter your rent "))
# else :
#     user_rent = 0
#
# user_ke_bill =  int(input("Enter Your Ke bill expence : "))
# user_grocery =  int(input("Enter Your grocery expence : "))
# user_gas =  int(input("Enter Your gas bill expence : "))
# user_water_bill =  int(input("Enter Your Water bill expence : "))
# user_internet =  int(input("Enter Your internet bill expence : "))
# user_jamedar_bill =  int(input("Enter Your jamedar bill expence : "))
#
#
# total_expence = user_ke_bill + user_grocery + user_gas + user_water_bill +  user_internet + user_jamedar_bill + user_rent
#
#
# print(total_expence)

# List
#
# dishesList = ["Biryani", "Pulao", "Karahi", "Qorma", "Nihari", "Haleem", "Halwa Puri", "Paya", "Keema", "Zarda"]
#
# #Functions
#
# print(f"Dishes List: {dishesList}")
#
# print(f"Number of Dishes: {len(dishesList)}")
#
# print(f"{dishesList[2]}")
#
# print(dishesList[3:7])
#
# print(dishesList[-2])
#
# dishesList.append("Qorma")
# print(f"after append: {dishesList}")
#
# dishesList.insert(4,"Payee")
# print(f"after insert: {dishesList}")
#
# sweetDish = ["Gulaab Jamun", "Kheer", "Jalebi"]
# dishesList.extend(sweetDish)
# print(f"After Add Sweet Dishes: {dishesList}")
#
# print(f"Number of Dishes: {len(dishesList)}")
#
# dishesList.sort()
# print(f"Assending Order : {dishesList}")
#
# dishesList.sort(reverse=True)
# print(f"Decending order : {dishesList}")
#
# dishesList.remove("Nihari")
# print(f"After Removing Nihari : {dishesList}")
#
# dishesList.pop()
# dishesList.pop()
# print(f"After pop : {dishesList}")
#
# sizeofDishes = len(dishesList)
# for a in range(sizeofDishes):
#     print(f"Dish : {dishesList[a]}")


# myInfo = {
#     "name": "Saqib Ali",
#     "age": 19,
#     "city": "Karachi",
#     "cnic": 4210137643781122,
#     "address": "Orangi Town, Karachi"
# }
#
# print(myInfo)
# myInfo["course"] = "Python"
# print(myInfo)
# print(myInfo.keys())
# print(myInfo.values())
# del myInfo["cnic"]
# print(myInfo)

import  pandas
# Student = {
#     "name": [
#         "Muhammad Raza", "Ahmed", "Ali", "Usman", "Hassan",
#         "Fatima", "Zainab", "Ayesha", "Umar", "Bilal"
#     ],
#     "age": [20, 21, 22, 20, 19, 21, 23, 22, 20, 18],
#     "city": [
#         "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Quetta",
#         "Peshawar", "Multan", "Faisalabad", "Hyderabad", "Sialkot"
#     ],
#     "cnic": [
#         42101376437822, 3520212345678, 6110111122223, 3740512345678, 4220156789123,
#         4250198765432, 3730211223344, 4210188888888, 3520211111111, 6110199999999
#     ],
#     "address": [
#         "North Nazimabad, Karachi", "Model Town, Lahore", "G-11, Islamabad", "Saddar, Rawalpindi", "Satellite Town, Quetta",
#         "Hayatabad, Peshawar", "Shah Rukn Alam, Multan", "Peoples Colony, Faisalabad", "Latifabad, Hyderabad", "Cantt, Sialkot"
#     ],
#     "email": [
#         "raza@gmail.com", "ahmed@gmail.com", "ali@yahoo.com", "usman@hotmail.com", "hassan@gmail.com",
#         "fatima@yahoo.com", "zainab@gmail.com", "ayesha@hotmail.com", "umar@yahoo.com", "bilal@gmail.com"
#     ],
#     "phone": [
#         "03001234567", "03019876543", "03121234567", "03219874567", "03331234567",
#         "03451239876", "03561234567", "03671234567", "03781234567", "03891234567"
#     ],
#     "gender": [
#         "Male", "Male", "Male", "Male", "Male",
#         "Female", "Female", "Female", "Male", "Male"
#     ],
#     "education": [
#         "Matric", "Inter", "Bachelor", "Matric", "Inter",
#         "Bachelor", "Master", "PhD", "Bachelor", "Inter"
#     ],
#     "is_active": [
#         True, True, False, True, False,
#         True, True, False, True, True
#     ]
# }
#
# print(Student)
# dFrame = pandas.DataFrame(Student)
# print(dFrame)

import pandas as pd

# Sample data
product_name = ["Headphone", "Mouse", "Keyboard", "Monitor", "Speaker"]
price = [1500, 800, 1200, 10000, 2500]
brand = ["Sony", "Logitech", "HP", "Dell", "JBL"]
category = ["Audio", "Peripheral", "Peripheral", "Display", "Audio"]

# Create dictionary
Products = {
    "Product Name": product_name,
    "Price (PKR)": price,
    "Brand": brand,
    "Category": category
}

# Create DataFrame
product_table = pd.DataFrame(Products)

# add Column

product_table["stock"] = "Available"


# Print dictionary and DataFrame
print(Products)
print(product_table)
#   print price grater than 1000
print(product_table[product_table["Price (PKR)"] >= 1000])
print(product_table[product_table["Category"] == "Audio"])
print(product_table[
          (product_table["Brand"] == "Dell")
    &
          (product_table["Price (PKR)"] >= 1500)
      ])

product_table.to_csv("ProductData.csv", index= False)