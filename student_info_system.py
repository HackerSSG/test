class Student:
    def __init__(self, roll_number, name, grade, class_name):
        self.roll_number = roll_number
        self.name = name
        self.grade = grade
        self.class_name = class_name

    def display_student(self):
        return f"Roll No: {self.roll_number}, Name: {self.name}, Grade: {self.grade}, Class: {self.class_name}"


class StudentInformationSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students:
                print(student.display_student())

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(student.display_student())
                return
        print("Student not found.")

    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student removed successfully.")
                return
        print("Student not found.")


if __name__ == "__main__":
    sis = StudentInformationSystem()

    while True:
        print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            roll_number = int(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")
            class_name = input("Enter Class Name: ")
            student = Student(roll_number, name, grade, class_name)
            sis.add_student(student)

        elif choice == 2:
            sis.view_students()

        elif choice == 3:
            roll_number = int(input("Enter Roll Number: "))
            sis.search_student(roll_number)

        elif choice == 4:
            roll_number = int(input("Enter Roll Number: "))
            sis.delete_student(roll_number)

        elif choice == 5:
            print("Exiting Program.")
            break

        else:
            print("Invalid choice. Please try again.")
