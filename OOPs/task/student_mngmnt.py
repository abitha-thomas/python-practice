# Student management system

# Create a class called Student that has the following attributes:
# student_id
# name

# Create a class called GraduateStudent that inherits from the Student class and has the following attributes:
# course

# Create a class called StudentSystem that has the following methods:
# add_student
# search_student
# delete_student
# update_student
# display_all_students
# exit

# Exception handling for invalid input

class Student:
    def __init__(self,student_id,name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"ID : {self.student_id} ,Name: {self.name}"

class GraduateStudent(Student):
    def __init__(self, student_id, name, course):
        super().__init__(student_id, name)
        self.course = course
        
    def __str__(self):
        return f"ID : {self.student_id} ,Name: {self.name}, Course: {self.course}"

class StudentSystem:
    def __init__(self):
        self.students = {}
        
    def add_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
            if student_id in self.students:
                raise ValueError("Student ID already exists!")

            name = input("Enter Name: ")
            choice = input("Is Graduate Student? (yes/no): ").lower()

            if choice == "yes":
                course = input("Enter Course: ")
                student = GraduateStudent(student_id, name, course)
            else:
                student = Student(student_id, name)

            self.students[student_id] = student
            print("Student added successfully!")
        except ValueError as e:
            print(e)

    def search_student(self):
        student_id = int(input("Enter Student ID: "))
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print("Student not found!")

    def delete_student(self):
        student_id = int(input("Enter Student ID: "))
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    def update_student(self):
            student_id = int(input("Enter Student ID: "))
            if student_id in self.students:
                choice = input("Do you want to change student name, student ID or graduate course? (name/id/course): ").lower()
                if choice == "name":
                    name = input("Enter new Name: ")
                    self.students[student_id].name = name
                elif choice == "id":
                    new_id = int(input("Enter new Student ID: "))
                    if new_id not in self.students:
                        self.students[new_id] = self.students.pop(student_id)
                    else:
                        print("Student ID already exists!")
                elif choice == "course":
                    if isinstance(self.students[student_id], GraduateStudent):
                        course = input("Enter new Course: ")
                        self.students[student_id].course = course
                    else:
                        add_graduation = input("Do you want to add graduation to this student? (yes/no): ").lower()
                        if add_graduation == "yes":
                            course = input("Enter Course: ")
                            self.students[student_id] = GraduateStudent(student_id, self.students[student_id].name, course)
                        else:
                            print("Student is not a graduate student!")
                            print("---------------------------------")
                else:
                    print("Invalid choice!")
            else:
                print("Student not found!")

    def display_all_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students.values():
                print(student)


def main():
    student_system = StudentSystem()
    while True:
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Display All Students")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_system.add_student()
        elif choice == "2":
            student_system.search_student()
        elif choice == "3":
            student_system.delete_student()
        elif choice == "4":
            student_system.update_student()
        elif choice == "5":
            student_system.display_all_students()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()