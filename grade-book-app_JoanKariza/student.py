#!/usr/bin/python3
class Student:
    """Class to represent a student."""

    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0

    def calculate_GPA(self):
        """Calculate the GPA of the student based on registered courses."""
        if not self.courses_registered:
            self.GPA = 0.0
            return
        total_credits = 0
        total_points = 0
        for course, grade in self.courses_registered.items():
            total_credits += course.credits
            total_points += grade * course.credits
        self.GPA = total_points / total_credits

    def register_for_course(self, course, grade):
        """Register a student for a course with the given grade."""
        self.courses_registered[course] = grade
        self.calculate_GPA()
