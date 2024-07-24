#!/usr/bin/python3
class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self):
        # Add a new student to the gradebook
        email = input("Enter student email: ")
        names = input("Enter student names: ")
        student = Student(email, names)
        self.student_list.append(student)
        print(f"Student {names} added successfully.")

    def add_course(self):
        # Add a new course to the gradebook
        name = input("Enter course name: ")
        trimester = input("Enter trimester: ")
        credits = int(input("Enter credits: "))
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        print(f"Course {name} added successfully.")

    def register_student_for_course(self):
        # Register an existing student for an existing course
        email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        student = next((s for s in self.student_list if s.email == email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course)
            print(f"{student.names} registered for {course.name}.")
        else:
            print("Student or course not found.")

    def save_student_grade(self):
        # Save a grade for a student in a specific course
        email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        grade = float(input("Enter grade: "))
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            for i, (course, _) in enumerate(student.courses_registered):
                if course.name == course_name:
                    student.courses_registered[i] = (course, grade)
                    print(f"Grade saved for {student.names} in {course_name}.")
                    return
            print("Course not found for this student.")
        else:
            print("Student not found.")

    def calculate_ranking(self):
        # Calculate and display the ranking of students based on GPA
        for student in self.student_list:
            student.calculate_gpa()
        self.student_list.sort(key=lambda s: s.gpa, reverse=True)
        for i, student in enumerate(self.student_list, 1):
            print(f"{i}. {student.names}: GPA {student.gpa:.2f}")

    def search_by_grade(self):
        # Search and display students within a specified GPA range
        min_grade = float(input("Enter minimum GPA: "))
        max_grade = float(input("Enter maximum GPA: "))
        filtered_students = [s for s in self.student_list if min_grade <= s.gpa <= max_grade]
        for student in filtered_students:
            print(f"{student.names}: GPA {student.gpa:.2f}")

    def generate_transcript(self):
        # Generate and display a transcript for a specific student
        email = input("Enter student email: ")
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            print(f"\nTranscript for {student.names}")
            print(f"Email: {student.email}")
            print("Courses:")
            for course, grade in student.courses_registered:
                print(f"- {course.name}: Grade {grade}")
            print(f"GPA: {student.gpa:.2f}")
        else:
            print("Student not found.")
