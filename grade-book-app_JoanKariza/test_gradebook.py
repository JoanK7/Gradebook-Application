#!/usr/bin/python3
import unittest
from student import Student
from course import Course
from gradebook_class import Registration

class TestGradeBook(unittest.TestCase):
    def test_student_creation(self):
        student = Student("j.kariza@alustudent.com", "Joan Kariza")
        student.save_to_csv()
        with open('students.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            found = False
            for row in reader:
                if row == ["j.kariza@alustudent.com", "Joan Kariza"]:
                    found = True
                    break
            self.assertTrue(found)

    def test_course_creation(self):
        course = Course("BSE", "January 2024", 3)
        course.save_to_csv()
        with open('courses.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            found = False
            for row in reader:
                if row == ["BSE", "January 2024", "3"]:
                    found = True
                    break
            self.assertTrue(found)

    def test_registration(self):
        registration = Registration("j.kariza@alustudent.com", "BSE", "A")
        registration.save_to_csv()
        with open('registrations.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            found = False
            for row in reader:
                if row == ["j.kariza@alustudent.com", "BSE", "A"]:
                    found = True
                    break
            self.assertTrue(found)

    def test_gpa_calculation(self):
        gpa = Registration.calculate_gpa("j.kariza@alustudent.com")
        self.assertIsNotNone(gpa)
        self.assertAlmostEqual(gpa, 4.0, places=1)

    def test_search_by_gpa(self):
        # Ensure some registrations exist
        student = Student("student@example.com", "Test Student")
        student.save_to_csv()
        course = Course("Test Course", "Fall 2023", 3)
        course.save_to_csv()
        registration = Registration("student@example.com", "Test Course", "A")
        registration.save_to_csv()

        results = Registration.search_by_gpa(3.5, 4.0)
        self.assertGreater(len(results), 0)

if __name__ == "__main__":
    unittest.main()
