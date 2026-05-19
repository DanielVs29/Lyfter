def add_students(students):

    while True:

        new_student = {
            "name": valid_name(),
            "section": valid_section(),
            "spanish_grade": valid_grade("Spanish"),
            "english_grade": valid_grade("English"),
            "science_grade": valid_grade("Science"),
            "socials_grade": valid_grade("Socials")
        }

        exists = False

        for student in students:

            if (
                student['name'].lower() == new_student['name'].lower()
                and
                student['section'].lower() == new_student['section'].lower()
            ):

                print(f"\nError: Student {new_student['name']} already exists.\n")
                exists = True
                break

        if not exists:
            students.append(new_student)
            print("Student added successfully.\n")

        new = input("Do you want to add another student? (yes/no): ").lower()

        if new != "yes":
            break


def show_students(students):
    if not students:
        print("No students to show.\n")
        return

    for student in students:
        print("---------------------------------------------")
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish Grade: {student['spanish_grade']}")
        print(f"English Grade: {student['english_grade']}")
        print(f"Science Grade: {student['science_grade']}")
        print(f"Socials Grade: {student['socials_grade']}")
        print("---------------------------------------------")


def top3_average(students):
    if not students:
        print("No students to calculate averages.\n")
        return

    for student in students:
        average = (student['spanish_grade'] + student['english_grade'] +
                   student['science_grade'] + student['socials_grade']) / 4
        student['average'] = average

    sorted_students = sorted(students, key=lambda x: x['average'], reverse=True)
    top3 = sorted_students[:3]

    print("Top 3 Students by Average Grade:")
    for student in top3:
        print(f"Name: {student['name']} - Average Grade: {student['average']}")


def all_students_average(students):
    if not students:
        print("No students to calculate averages.\n")
        return

    for student in students:
        average = (student['spanish_grade'] + student['english_grade'] +
                   student['science_grade'] + student['socials_grade']) / 4
        student['average'] = average

    total_average = 0

    for student in students:
        total_average += student['average']

    print("---------------------------------------------")
    print(f"Average grade of all students: {total_average / len(students)}")
    print("---------------------------------------------")


def delete_student(students):

    name = input("Enter the name of the student to delete: ")

    for student in students:

        if student['name'].lower() == name.lower():
            print(f"Do you want to delete the student {name}?")

            confirm = input("Enter 'yes' to confirm deletion: ").lower()

            if confirm == "yes":
                students.remove(student)
                print(f"Student {name} deleted successfully.\n")
            return
    print(f"Student {name} not found in the list.\n")


def failed_students(students):

    if not students:
        print("No students found.\n")
        return

    found_failed = False

    for student in students:

        failed_subjects = []

        if student['spanish_grade'] < 60:
            failed_subjects.append(f"Spanish: {student['spanish_grade']}")

        if student['english_grade'] < 60:
            failed_subjects.append(f"English: {student['english_grade']}")

        if student['science_grade'] < 60:
            failed_subjects.append(f"Science: {student['science_grade']}")

        if student['socials_grade'] < 60:
            failed_subjects.append(f"Socials: {student['socials_grade']}")

        if failed_subjects:

            if not found_failed:
                print("Failed Students:\n")

            found_failed = True

            print(f"Name: {student['name']} - Section: {student['section']}")
            print("Failed Subjects:")

            for subject in failed_subjects:
                print(f"  {subject}")

            print("---------------------------------------------")

    if not found_failed:
        print("There are no failed students.\n")

def valid_grade(subject):

    while True:

        try:
            grade = float(input(f"Enter {subject} grade: "))

            if 0 <= grade <= 100:
                return grade

            print("Grade must be between 0 and 100.\n")

        except ValueError:
            print("Please enter a valid number.\n")


def valid_name():

    while True:

        name = input("Enter student's name: ").strip()

        if is_valid_name(name):
            return name

        print("Invalid name. Name cannot contain numbers.\n")


def is_valid_name(name):

    if not name.strip():
        return False

    for character in name:

        if character.isdigit():
            return False

    return True


def valid_section():

    while True:

        section = input("Enter student's section: ").strip()

        if section and is_valid_section(section):
            return section

        print("Please enter a valid section.\n")


def is_valid_section(section):

    if len(section) < 2:
        return False

    numbers = section[:-1]
    letter = section[-1]

    if not numbers.isdigit():
        return False

    if not letter.isalpha():
        return False

    return True