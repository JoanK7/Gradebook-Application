#!/usr/bin/python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.gpa = 0.0

    def calculate_gpa(self):
        # Calculate the GPA based on registered courses and grades
        if not self.courses_registered:
            return 0.0
        total_credits = 0
        total_grade_points = 0
        for course, grade in self.courses_registered:
            total_credits += course.credits
            total_grade_points += grade * course.credits
        self.gpa = total_grade_points / total_credits
        return self.gpa

    def register_for_course(self, course):
        # Register the student for a course with an initial grade of 0
        self.courses_registered.append((course, 0))
