#!/usr/bin/python3
from gradebook_class import GradeBook

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
