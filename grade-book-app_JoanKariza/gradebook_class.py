#!/usr/bin/python3
import csv
from student import Student
from course import Course

class Registration:
    def __init__(self, student_email, course_name, grade):
        self.student_email = student_email
        self.course_name = course_name
        self.grade = grade

    def save_to_csv(self):
        with open('registrations.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.student_email, self.course_name, self.grade])

    @staticmethod
    def calculate_gpa(student_email):
        with open('registrations.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            grades = []
            credits = []
            for row in reader:
                if row[0] == student_email:
                    grade = row[2]
                    course_name = row[1]
                    grades.append(Registration.convert_grade_to_points(grade))
                    credits.append(Course.get_course_credits(course_name))
            if credits:
                total_points = sum(g * c for g, c in zip(grades, credits))
                total_credits = sum(credits)
                gpa = total_points / total_credits if total_credits > 0 else 0
                return gpa
            else:
                return None

    @staticmethod
    def convert_grade_to_points(grade):
        grade_map = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        return grade_map.get(grade, 0.0)

    @staticmethod
    def search_by_gpa(min_gpa, max_gpa):
        results = []
        with open('students.csv', 'r') as student_file:
            students = {row[0]: row[1] for row in csv.reader(student_file)}

        with open('registrations.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            gpa_dict = {}
            for row in reader:
                student_email = row[0]
                gpa = Registration.calculate_gpa(student_email)
                if gpa is not None and min_gpa <= gpa <= max_gpa:
                    gpa_dict[student_email] = gpa

        for email, gpa in gpa_dict.items():
            results.append(f">> {students[email]} (GPA: {gpa:.2f})")

        return results
