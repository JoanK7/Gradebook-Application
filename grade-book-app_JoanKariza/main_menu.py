#!/usr/bin/python3
def main():
    # Main program to interact with the gradebook
    gradebook = GradeBook()

    while True:
        # Display menu options for the user
        print("\nGrade Book Menu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new student
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
        elif choice == '2':
            # Add a new course
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        elif choice == '3':
            # Register a student for a course with a grade
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(student_email, course_name, grade)
        elif choice == '4':
            # Calculate the GPA for each student
            gradebook.calculate_GPA()
        elif choice == '5':
            # Calculate and display the ranking of students
            gradebook.calculate_ranking()
        elif choice == '6':
            # Search students by GPA range
            min_gpa = float(input("Enter minimum GPA: "))
            max_gpa = float(input("Enter maximum GPA: "))
            students = gradebook.search_by_grade(min_gpa, max_gpa)
            for student in students:
                print(f"{student.email}: {student.GPA}")
        elif choice == '7':
            # Generate and display transcripts for all students
            gradebook.generate_transcript()
        elif choice == '8':
            # Exit the program
            break
        else:
            # Handle invalid choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
