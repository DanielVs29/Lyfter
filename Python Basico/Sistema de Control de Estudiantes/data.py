import csv

def save_students_csv(file_path, students):

    if not students:
        print("No students to save.\n")
        return

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = students[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(students)
        print("Students saved successfully.\n")

def load_students_csv(file_path):
    new_students = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for student in reader:
                student = {
                    "name": student["name"],
                    "section": student["section"],
                    "spanish_grade": float(student["spanish_grade"]),
                    "english_grade": float(student["english_grade"]),
                    "science_grade": float(student["science_grade"]),
                    "socials_grade": float(student["socials_grade"])
                }
                new_students.append(student)

            print("Students loaded successfully.\n")

    except FileNotFoundError:
        print(f"The file {file_path} was not found.\n")
    except Exception as e:
        print(f"Error loading students from CSV: {e}\n")
    
    return new_students
