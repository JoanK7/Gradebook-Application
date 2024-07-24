#!/usr/bin/python3
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

def main():
    """Main function to run the GradeBook application."""
    gradebook = GradeBook()

    while True:
        print("\nGradeBook Menu")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(student_email, course_name, grade)
        elif choice == '4':
            ranking = gradebook.calculate_ranking()
            for student in ranking:
                print(f"{student.email} - GPA: {student.GPA}")
        elif choice == '5':
            min_gpa = float(input("Enter minimum GPA: "))
            max_gpa = float(input("Enter maximum GPA: "))
            results = gradebook.search_by_grade(min_gpa, max_gpa)
            for student in results:
                print(f"{student.email} - GPA: {student.GPA}")
        elif choice == '6':
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            print(transcript)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
