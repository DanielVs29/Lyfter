from actions import add_students, show_students, top3_average, grade_average, delete_student, failed_students
from data import save_students_csv, load_students_csv

def start_menu(students):

    option = ""

    while option != "9":

        option = input(
            "Please select an option:\n"
            "1. Add Students\n"
            "2. Students Information\n"
            "3. Top 3 Average\n"
            "4. Grade Average\n"
            "5. Save Students to CSV\n"
            "6. Load Students from CSV\n"
            "7. Delete Student\n"
            "8. Failed Students\n"
            "9. Exit\n\n"
        )

        if option == "1":
            add_students(students)

        elif option == "2":
            show_students(students)

        elif option == "3":
            top3_average(students)

        elif option == "4":
            grade_average(students)

        elif option == "5":
            save_students_csv("students.csv", students)

        elif option == "6":
            students = load_students_csv("students.csv")

        elif option == "7":
            delete_student(students)

        elif option == "8":
            failed_students(students)

        elif option == "9":
            print("Closing program...")

        else:
            print("Invalid option, please try again.\n")