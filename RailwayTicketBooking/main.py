class RailwayTicketBooking:
    def __init__(self):
        self.confirmed_tickets = []
        self.rac_tickets = []
        self.waiting_list = []
        self.confirmed_limit = 63
        self.rac_limit = 18
        self.waiting_limit = 10
        self.seatNo = 0
        self.no_of_Lower_Berth = 0
        self.limit_of_Lower_Berth = 21  # 1/3rd of 63
        self.no_of_Upper_Berth = 0
        self.limit_of_Upper_Berth = 21  # 1/3rd of 63
        self.no_of_Middle_Berth = 0
        self.limit_of_Middle_Berth = 21  # 1/3rd of 63
        self.passengerId = 0

    def book_ticket(self, name, age, gender, berth_preference):
        """Books a ticket for the passenger with the given details."""
        self.passengerId += 1
        self.seatNo += 1
        ticket = {
            "Passenger ID": self.passengerId,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Berth_preference": berth_preference,
            "SeatNo": self.seatNo,
        }

        # Check if the passenger is a child below age 5
        if age < 5:
            print(f"Ticket not allocated for {name} (Age: {age}). Details stored only.")
            return

        # Check if confirmed tickets are available
        if len(self.confirmed_tickets) < self.confirmed_limit:
            # Assign appropriate berths based on preference and availability
            if age > 60 or (
                    gender == 'F' and berth_preference == 'L' and self.no_of_Lower_Berth < self.limit_of_Lower_Berth):
                ticket["Berth"] = "Lower"
                self.no_of_Lower_Berth += 1
            elif berth_preference == 'L' and self.no_of_Lower_Berth < self.limit_of_Lower_Berth:
                ticket["Berth"] = "Lower"
                self.no_of_Lower_Berth += 1
            elif berth_preference == 'U' and self.no_of_Upper_Berth < self.limit_of_Upper_Berth:
                ticket["Berth"] = "Upper"
                self.no_of_Upper_Berth += 1
            elif berth_preference == 'M' and self.no_of_Middle_Berth < self.limit_of_Middle_Berth:
                ticket["Berth"] = "Middle"
                self.no_of_Middle_Berth += 1
            else:
                # Assign any available berth if preferred one is not available
                if self.no_of_Lower_Berth < self.limit_of_Lower_Berth:
                    ticket["Berth"] = "Lower"
                    self.no_of_Lower_Berth += 1
                elif self.no_of_Upper_Berth < self.limit_of_Upper_Berth:
                    ticket["Berth"] = "Upper"
                    self.no_of_Upper_Berth += 1
                elif self.no_of_Middle_Berth < self.limit_of_Middle_Berth:
                    ticket["Berth"] = "Middle"
                    self.no_of_Middle_Berth += 1
            self.confirmed_tickets.append(ticket)
            print(f"Ticket {name} is booked for {age} and {gender}.")
        # Check if RAC tickets are available
        elif len(self.rac_tickets) < self.rac_limit:
            ticket["Berth"] = "Side-Lower"
            self.rac_tickets.append(ticket)
        # Check if waiting list tickets are available
        elif len(self.waiting_list) < self.waiting_limit:
            self.waiting_list.append(ticket)
        else:
            print("No tickets available")

    def cancel_ticket(self, passenger_id):
        """Cancels the ticket for the given Passenger ID."""
        for ticket_list in [self.confirmed_tickets, self.rac_tickets, self.waiting_list]:
            for ticket in ticket_list:
                if ticket["Passenger ID"] == passenger_id:
                    ticket_list.remove(ticket)
                    print(f"Cancelled ticket for Passenger ID: {passenger_id}")
                    self.update_tickets()
                    return
        print(f"No ticket found for Passenger ID: {passenger_id}")

    def update_tickets(self):
        """Updates the ticket statuses when a confirmed ticket is canceled."""
        # Move RAC ticket to confirmed if space available
        if self.rac_tickets and len(self.confirmed_tickets) < self.confirmed_limit:
            rac_ticket = self.rac_tickets.pop(0)
            self.adjust_berth_count(rac_ticket["Berth"], increment=True)
            self.confirmed_tickets.append(rac_ticket)

        # Move waiting list ticket to RAC if space available
        if self.waiting_list and len(self.rac_tickets) < self.rac_limit:
            waiting_ticket = self.waiting_list.pop(0)
            waiting_ticket["Berth"] = "Side-Lower"
            self.rac_tickets.append(waiting_ticket)

    def adjust_berth_count(self, berth, increment):
        """Adjusts the berth count when a ticket is booked or canceled."""
        if berth == "Lower":
            if increment:
                self.no_of_Lower_Berth += 1
            else:
                self.no_of_Lower_Berth -= 1
        elif berth == "Upper":
            if increment:
                self.no_of_Upper_Berth += 1
            else:
                self.no_of_Upper_Berth -= 1
        elif berth == "Middle":
            if increment:
                self.no_of_Middle_Berth += 1
            else:
                self.no_of_Middle_Berth -= 1

    def print_booked_tickets(self):
        """Prints the details of all booked tickets."""
        print("Confirmed Tickets:")
        for ticket in self.confirmed_tickets:
            print(ticket)
        print(f"Total confirmed tickets: {len(self.confirmed_tickets)}")

        print("\nRAC Tickets:")
        for ticket in self.rac_tickets:
            print(ticket)
        print(f"Total RAC tickets: {len(self.rac_tickets)}")

        print("\nWaiting List Tickets:")
        for ticket in self.waiting_list:
            print(ticket)
        print(f"Total waiting list tickets: {len(self.waiting_list)}")

    def print_available_tickets(self):
        """Prints the number of available tickets in each category."""
        available_confirmed = self.confirmed_limit - len(self.confirmed_tickets)
        available_rac = self.rac_limit - len(self.rac_tickets)
        available_waiting = self.waiting_limit - len(self.waiting_list)

        print(f"Available Confirmed Tickets: {available_confirmed}")
        print(f"Available RAC Tickets: {available_rac}")
        print(f"Available Waiting List Tickets: {available_waiting}")


def main():
    system = RailwayTicketBooking()
    while True:
        print("\nRailway Ticket Booking System")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Print Booked Tickets")
        print("4. Print Available Tickets")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter passenger name: ")
            try:
                age = int(input("Enter passenger age: "))
            except ValueError:
                print("Invalid age! Please enter a valid number.")
                continue
            gender = input("Enter passenger gender (M/F): ").upper()
            berth_preference = input("Enter berth preference (L/U/M): ").upper()
            system.book_ticket(name, age, gender, berth_preference)
        elif choice == "2":
            try:
                passenger_id = int(input("Enter Passenger ID to cancel: "))
            except ValueError:
                print("Invalid Passenger ID! Please enter a valid number.")
                continue
            system.cancel_ticket(passenger_id)
        elif choice == "3":
            system.print_booked_tickets()
        elif choice == "4":
            system.print_available_tickets()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
