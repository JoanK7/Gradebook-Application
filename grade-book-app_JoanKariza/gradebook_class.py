#!/usr/bin/python3
from student import Student
from course import Course

class GradeBook:
    """Class to manage the grade book."""

    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        """Add a student to the grade book."""
        new_student = Student(email, names)
        self.student_list.append(new_student)

    def add_course(self, name, trimester, credits):
        """Add a course to the grade book."""
        new_course = Course(name, trimester, credits)
        self.course_list.append(new_course)

    def register_student_for_course(self, student_email, course_name, grade):
        """Register a student for a course."""
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)

    def calculate_ranking(self):
        """Calculate the ranking of students based on GPA."""
        return sorted(self.student_list, key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, min_gpa, max_gpa):
        """Search for students within a GPA range."""
        return [s for s in self.student_list if min_gpa <= s.GPA <= max_gpa]

    def generate_transcript(self, student_email):
        """Generate a transcript for a student."""
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            transcript = f"Transcript for {student.names} ({student.email}):\n"
            for course, grade in student.courses_registered.items():
                transcript += f"{course.name}: {grade}\n"
            transcript += f"GPA: {student.GPA}"
            return transcript
        return "Student not found."
