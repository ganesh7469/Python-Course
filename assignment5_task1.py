

'''Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''

student_marks = {
    "Anshuman": 85,
    "Adi": 78,
    "Akhanda": 92
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")