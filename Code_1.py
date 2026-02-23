class ClinicAppointment:
    def __init__(self):
        self.slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.appointments = {}

    def book_appointment(self):
        Name = input("Enter Patient Name: ")
        Age = input("Enter Patient Age: ")
        Mobile = input("Enter Mobile Number: ")
        Doctor = input("Enter Preferred Doctor: ")
        print("\nAvailable Time Slots:")
        for i, j in enumerate(self.slots, 1):
            print(f"{i}. {j}")
        choice = int(input("Choose slot number: "))
        Slot = self.slots[choice - 1]

        if Doctor not in self.appointments:
            self.appointments[Doctor] = {j: [] for j in self.slots}
        if len(self.appointments[Doctor][Slot]) >= 3:
            print("Choose Another Doctor!!")
            return

        record = {"Name": Name, "Age": Age, "Mobile": Mobile, "Doctor": Doctor, "Slot": Slot}

        self.appointments[Doctor][Slot].append(record)
        print("Appointment Booked Successfully!!")

    def view_appointment(self):
        Mobile = input("Enter Mobile Number: ")
        present = False
        for Doctor in self.appointments:
            for Slot in self.appointments[Doctor]:
                for rec in self.appointments[Doctor][Slot]:
                    if rec["Mobile"] == Mobile:
                        print("\nAppointment Details:")
                        print(rec)
                        present = True
        if not present:
            print("No appointment found.")

    def cancel_appointment(self):
        Mobile = input("Enter Mobile number: ")
        for Doctor in self.appointments:
            for Slot in self.appointments[Doctor]:
                for rec in self.appointments[Doctor][Slot]:
                    if rec["Mobile"] == Mobile:
                        self.appointments[Doctor][Slot].remove(rec)
                        print("Appointment Cancelled!!")
                        return
        print("No appointment found.")

clinic = ClinicAppointment()

while True:
    print("\n***** Clinic Appointment System *****\n")
    print("1. Book Appointment")
    print("2. View Appointment")
    print("3. Cancel Appointment")
    print("4. Exit")

    ch = input("\nEnter choice: ")
    if ch == "1":
        clinic.book_appointment()
    elif ch == "2":
        clinic.view_appointment()
    elif ch == "3":
        clinic.cancel_appointment()
    elif ch == "4":
        break
    else:
        print("Invalid choice!")