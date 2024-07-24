#!/usr/bin/python3
import csv
from student import Student
from course import Course
from gradebook_class import Registration

def add_student():
    email = input("Enter student email: ")
    name = input("Enter student names: ")
    student = Student(email, name)
    student.save_to_csv()
    print("Student record created successfully!")

def add_course():
    name = input("Enter course name: ")
    trimester = input("Enter course trimester: ")
    credits = float(input("Enter course credits: "))
    course = Course(name, trimester, credits)
    course.save_to_csv()
    print("Course record created successfully!")

def register_student_for_course():
    student_email = input("Enter student email: ")
    course_name = input("Enter course name: ")
    grade = input("Enter grade: ")
    registration = Registration(student_email, course_name, grade)
    registration.save_to_csv()
    print("Student registered for course successfully!")

def calculate_ranking():
    email = input("Enter student email to calculate GPA: ")
    gpa = Registration.calculate_gpa(email)
    if gpa is not None:
        print(f"The GPA for {email} is {gpa:.2f}")
    else:
        print(f"No grades found for student with email {email}")

def search_by_gpa():
    min_gpa = float(input("Enter minimum GPA: "))
    max_gpa = float(input("Enter maximum GPA: "))
    results = Registration.search_by_gpa(min_gpa, max_gpa)
    if results:
        print("Search results:")
        for result in results:
            print(result)
    else:
        print("No students found with GPA in the specified range.")

def generate_transcript():
    email = input("Enter student email to generate transcript: ")
    with open('registrations.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        print(f"Transcript for {email}:")
        for row in reader:
            if row[0] == email:
                print(f"Course: {row[1]}, Grade: {row[2]}")
        gpa = Registration.calculate_gpa(email)
        if gpa is not None:
            print(f"GPA: {gpa:.2f}")

def main():
    while True:
        print("\nWelcome to the Grade Book Application!")
        print("Please select an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by GPA")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            register_student_for_course()
        elif choice == '4':
            calculate_ranking()
        elif choice == '5':
            search_by_gpa()
        elif choice == '6':
            generate_transcript()
        elif choice == '7':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
