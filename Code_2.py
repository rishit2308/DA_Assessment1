class SchoolManagement:
    def __init__(self):
        self.students = {}        
        self.next_id = 1          
        
    def valid_age(self, Age):
        return 5 <= Age <= 18

    def valid_mobile(self, Mobile):
        return Mobile.isdigit() and len(Mobile) == 10

    def new_admission(self):
        Name = input("\nEnter student name: ")
        Age = int(input("Enter age: "))
        if not self.valid_age(Age):
            print("\nAge must be between 5 and 18.")
            return

        student_class = int(input("Enter class (1-12): "))
        if student_class < 1 or student_class > 12:
            print("\nInvalid class!!")
            return

        Mobile = input("Enter guardian mobile number: ")
        if not self.valid_mobile(Mobile):
            print("\nMobile Number must be of 10 digits!!")
            return

        student_id = self.next_id
        self.next_id += 1

        self.students[student_id] = {"Name": Name, "Age": Age, "Class": student_class, "Mobile Number": Mobile}
        print(f"Admission Successful!! Student ID: {student_id}")

    def view_student(self):
        id = int(input("\nEnter student ID to view: "))
        if id in self.students:
            print("\nStudent Details:")
            for i, j in self.students[id].items():
                print(f"{i}: {j}")
        else:
            print("Student not found.")

    def update_student(self):
        id = int(input("\nEnter student ID to update: "))
        if id not in self.students:
            print("Student not found.")
            return

        print("1. Update Mobile Number")
        print("2. Update Class")
        
        choice = input("\nChoose option: ")

        if choice == "1":
            Mobile = input("\nEnter new guardian mobile number: ")
            if self.valid_mobile(Mobile):
                self.students[id]["Mobile Number"] = Mobile
                print("Mobile Number updated.")
            else:
                print("Invalid Mobile Number!!")
        elif choice == "2":
            student_class = int(input("\nEnter new class (1-12): "))
            if 1 <= student_class <= 12:
                self.students[id]["Class"] = student_class
                print("Class updated.")
            else:
                print("Invalid class!!")
        else:
            print("Invalid choice.")

    def remove_student(self):
        id = int(input("\nEnter student ID to remove: "))
        if id in self.students:
            del self.students[id]
            print("Student record removed.")
        else:
            print("Student not found.")

school = SchoolManagement()

while True:
    print("\n***** School Management System *****\n")
    print("1. New Admission")
    print("2. View Student Details")
    print("3. Update Student Info")
    print("4. Remove Student Record")
    print("5. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        school.new_admission()
    elif choice == "2":
        school.view_student()
    elif choice == "3":
        school.update_student()
    elif choice == "4":
        school.remove_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")