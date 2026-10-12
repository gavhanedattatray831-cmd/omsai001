import openpyxl
import os

file = "student_marks.xlsx"

# Excel file create/open
if os.path.exists(file):
    wb = openpyxl.load_workbook(file)
    ws = wb.active
else:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Student Marks"
    ws.append(["Name", "Maths", "Science", "English",
               "Total", "Percentage", "Result"])

# Student details
name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# Calculation
total = maths + science + english
percentage = total / 3

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

# Excel me data add
ws.append([
    name,
    maths,
    science,
    english,
    total,
    round(percentage, 2),
    result
])

# Save
wb.save(file)

print("\nData successfully saved in Excel!")
print("Total:", total)
print("Percentage:", round(percentage, 2))
print("Result:", result)