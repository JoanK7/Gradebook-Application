#!/usr/bin/python
def main():
    # Main function to run the Gradebook application
    gradebook = GradeBook()

    while True:
        print("\nGradebook Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Save Student Grade")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            gradebook.add_student()
        elif choice == '2':
            gradebook.add_course()
        elif choice == '3':
            gradebook.register_student_for_course()
        elif choice == '4':
            gradebook.save_student_grade()
        elif choice == '5':
            gradebook.calculate_ranking()
        elif choice == '6':
            gradebook.search_by_grade()
        elif choice == '7':
            gradebook.generate_transcript()
        elif choice == '8':
            print("Thank you for using the Gradebook Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
