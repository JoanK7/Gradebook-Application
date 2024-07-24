import unittest
from gradebook_class import GradeBook
from student import Student
from course import Course

class TestGradeBook(unittest.TestCase):
    def setUp(self):
        self.gradebook = GradeBook()

    def test_add_student(self):
        self.gradebook.add_student("j.kariza@alustudent.com", "Joan Kariza")
        self.assertEqual(len(self.gradebook.student_list), 1)
        self.assertEqual(self.gradebook.student_list[0].email, "j.kariza@alustudent.com")

    def test_add_course(self):
        self.gradebook.add_course("BSE", "January 2024", 3)
        self.assertEqual(len(self.gradebook.course_list), 1)
        self.assertEqual(self.gradebook.course_list[0].name, "BSE")

    def test_register_student_for_course(self):
        self.gradebook.add_student("j.kariza@alustudent.com", "Joan Kariza")
        self.gradebook.add_course("BSE", "January 2024", 3)
        self.gradebook.register_student_for_course("j.kariza@alustudent.com", "BSE", 95)
        student = self.gradebook.student_list[0]
        self.assertEqual(student.courses_registered[self.gradebook.course_list[0]], 95)

    def test_calculate_ranking(self):
        self.gradebook.add_student("j.kariza@alustudent.com", "Joan Kariza")
        self.gradebook.add_student("jane.doe@example.com", "Jane Doe")
        self.gradebook.add_course("BSE", "January 2024", 3)
        self.gradebook.register_student_for_course("j.kariza@alustudent.com", "BSE", 95)
        self.gradebook.register_student_for_course("jane.doe@example.com", "BSE", 85)
        ranking = self.gradebook.calculate_ranking()
        self.assertEqual(ranking[0].email, "j.kariza@alustudent.com")

    def test_search_by_grade(self):
        self.gradebook.add_student("j.kariza@alustudent.com", "Joan Kariza")
        self.gradebook.add_course("BSE", "January 2024", 3)
        self.gradebook.register_student_for_course("j.kariza@alustudent.com", "BSE", 95)
        results = self.gradebook.search_by_grade(90, 100)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].email, "j.kariza@alustudent.com")

    def test_generate_transcript(self):
        self.gradebook.add_student("j.kariza@alustudent.com", "Joan Kariza")
        self.gradebook.add_course("BSE", "January 2024", 3)
        self.gradebook.register_student_for_course("j.kariza@alustudent.com", "BSE", 95)
        transcript = self.gradebook.generate_transcript("j.kariza@alustudent.com")
        self.assertIn("j.kariza@alustudent.com", transcript)

if __name__ == '__main__':
    unittest.main()

