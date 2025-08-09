# pip install firebase-admin
import firebase_admin
from firebase_admin import credentials, firestore

file_var = credentials.Certificate(r"C:\\Users\\asp\\Documents\\GitHub\\Aptech_Phyton_Practice\\PythonProject\\firebase_file.json")
firebase_admin.initialize_app(file_var)

collection_url = firestore.client()

print("----- Student Info ------\n")

name = input("Enter Your Name : ")
fathername = input("Enter Your Father Name : ")
contact = input("Enter Your Contact : ")
age = int(input("Enter Your age : "))

english_marks = float(input("Enter English Marks : "))
urdu_marks = float(input("Enter Urdu Marks : "))
computer_marks = float(input("Enter Computer Marks : "))
arts_marks = float(input("Enter Arts Marks : "))

total = english_marks + urdu_marks + arts_marks + computer_marks
percentage = (total * 100) / 400
grade = ""

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Fail"

Student_info = collection_url.collection("Student").document()
Student_info.set({
    "Name": name,
    "Father Name": fathername,
    "Contact": contact,
    "Age": age,
    "English Marks": english_marks,
    "Urdu Marks": urdu_marks,
    "Computer Marks": computer_marks,
    "Arts Marks": arts_marks,
    "Total": total,
    "Percentage": percentage,
    "Grade": grade
})

print("Data Saved Successfully")
