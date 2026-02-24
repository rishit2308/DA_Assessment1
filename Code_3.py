class BusReservation:
    def __init__(self):
        self.routes = {1: ("Mumbai to Pune", 500), 2: ("Delhi to Shimla", 800), 3: ("Bangalore to Chennai", 600), 4: ("Vadodara to Surat", 200)}

        self.tickets = {}           
        self.route_seats = {}       
        self.next_ticket_id = 101  

    def show_routes(self):
        print("\nAvailable Routes:")
        for i, j in self.routes.items():
            print(f"{i}. {j[0]} - ₹{j[1]}")

    def book_ticket(self):
        self.show_routes()

        choice = int(input("Select route number: "))
        if choice not in self.routes:
            print("Invalid route.")
            return

        Route, Price = self.routes[choice]

        Name = input("Enter Passenger Name: ")
        Age = int(input("Enter Age: "))
        Mobile = int(input("Enter Mobile Number: "))

        if Route not in self.route_seats:
            self.route_seats[Route] = []

        if len(self.route_seats[Route]) >= 40:
            print("Bus Full!!")
            return

        Seat = len(self.route_seats[Route]) + 1
        self.route_seats[Route].append(Seat)
        
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1

        self.tickets[ticket_id] = {"Name": Name, "Age": Age, "Mobile": Mobile, "Route": Route, "Seat": Seat, "Price": Price}

        print("\nTicket Booked!!")
        print(f"Ticket ID: {ticket_id}")
        print(f"Seat No: {Seat}")

    def view_ticket(self):
        id = int(input("\nEnter Ticket ID: "))
        if id in self.tickets:
            print("\nTicket Details:")
            for i, j in self.tickets[id].items():
                print(f"{i}: {j}")
        else:
            print("Ticket not found.")
            
    def cancel_ticket(self):
        id = int(input("\nEnter Ticket ID to cancel: "))
        if id in self.tickets:
            Route = self.tickets[id]["Route"]
            Seat = self.tickets[id]["Seat"]

            self.route_seats[Route].remove(Seat)

            del self.tickets[id]
            print("Ticket cancelled!!")
        else:
            print("Ticket not found.")

bus = BusReservation()

while True:
    print("\n***** Bus Reservation System *****")
    print("1. Show Available Routes")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    ch = input("\nEnter choice: ")

    if ch == "1":
        bus.show_routes()
    elif ch == "2":
        bus.book_ticket()
    elif ch == "3":
        bus.view_ticket()
    elif ch == "4":
        bus.cancel_ticket()
    elif ch == "5":
        break
    else:
        print("Invalid choice!!")