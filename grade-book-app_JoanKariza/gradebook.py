#!/usr/bin/python3
class GradeBook:
    def __init__(self):
        # Initialize the GradeBook with empty student and course lists
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        # Add a new student to the gradebook
        new_student = Student(email, names)
        self.student_list.append(new_student)

    def add_course(self, name, trimester, credits):
        # Add a new course to the gradebook
        new_course = Course(name, trimester, credits)
        self.course_list.append(new_course)

    def register_student_for_course(self, student_email, course_name, grade):
        # Register a student for a course with the specified grade
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)

    def calculate_GPA(self):
        # Calculate the GPA for each student in the gradebook
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        # Calculate and print the ranking of students based on their GPA
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        for rank, student in enumerate(self.student_list, start=1):
            print(f"{rank}. {student.email}: {student.GPA}")

    def search_by_grade(self, min_gpa, max_gpa):
        # Search and return students whose GPA falls within the specified range
        filtered_students = [s for s in self.student_list if min_gpa <= s.GPA <= max_gpa]
        return filtered_students

    def generate_transcript(self):
        # Generate and print the transcript for each student in the gradebook
        for student in self.student_list:
            print(f"Transcript for {student.names} ({student.email}):")
            for course, grade in student.courses_registered:
                print(f"  - {course.name}: {grade}")
            print(f"GPA: {student.GPA}")
