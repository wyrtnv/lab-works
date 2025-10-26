from openpyxl import Workbook
import os


FILE_NAME = 'students.xlsx'

HEADERS = ['Name', 'Age', 'Grade']

student_data = [
    ('John Smith', 18, 12),
    ('Emily Johnson', 17, 11),
    ('Michael Brown', 16, 10)
]

print(f"Attempting to create Excel file: '{FILE_NAME}'...")

try:
    workbook = Workbook()
    sheet = workbook.active

    sheet.append(HEADERS)

    for student in student_data:
        sheet.append(student)

    workbook.save(FILE_NAME)

    print(f"✅ File '{FILE_NAME}' successfully created and saved.")
    print(f"Path: {os.path.abspath(FILE_NAME)}")


except PermissionError:
    print(f"❌ Error: Permission denied. Cannot write file '{FILE_NAME}'.")
except Exception as e:
    print(
        f"❌ Error during file operation for '{FILE_NAME}': {type(e).__name__} - {e}")
