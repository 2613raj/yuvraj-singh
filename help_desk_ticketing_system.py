import re

class Ticket:
    counter = 2000

    def __init__(self, staff_id, ticket_creator_name, contact_email, description):
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.contact_email = contact_email
        self.description = description
        self.ticket_number = Ticket.counter + 1
        Ticket.counter += 1
        self.status = "Open"
        self.response = "Not Yet Provided"
        if "Password Change" in self.description:
            self.generate_new_password()

    def generate_new_password(self):
        new_password = self.staff_id[:2] + self.ticket_creator_name[:3]
        self.response = f"New password generated: {new_password}"
        self.close_ticket()

    def close_ticket(self):
        self.status = "Closed"

    def reopen_ticket(self):
        self.status = "Reopened"

    def update_response(self, response):
        self.response = response
        self.close_ticket()

    def print_ticket_info(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.ticket_creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}\n")

class TicketStats:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def resolve_ticket(self, ticket_number, response):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.update_response(response)
                break

    def reopen_ticket(self, ticket_number):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.reopen_ticket()
                break

    def print_ticket_statistics(self):
        total_tickets = len(self.tickets)
        resolved_tickets = len([ticket for ticket in self.tickets if ticket.status == "Closed"])
        open_tickets = total_tickets - resolved_tickets

        print("Displaying Ticket Statistics")
        print(f"Tickets Created: {total_tickets}")
        print(f"Tickets Resolved: {resolved_tickets}")
        print(f"Tickets To Solve: {open_tickets}\n")

    def print_all_tickets(self):
        print("Printing Tickets:")
        for ticket in self.tickets:
            ticket.print_ticket_info()


def main():
    ticket_stats = TicketStats()

    ticket1 = Ticket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
    ticket_stats.add_ticket(ticket1)

    ticket2 = Ticket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
    ticket_stats.add_ticket(ticket2)

    ticket3 = Ticket("JOHNS", "John", "john@whitecliffe.co.nz", "Password Change")
    ticket_stats.add_ticket(ticket3)

    ticket_stats.print_ticket_statistics()
    ticket_stats.print_all_tickets()

    ticket_stats.resolve_ticket(2001, "The monitor has been replaced.")
    ticket_stats.print_ticket_statistics()
    ticket_stats.print_all_tickets()

    ticket_stats.reopen_ticket(2001)
    ticket_stats.print_ticket_statistics()
    ticket_stats.print_all_tickets()

if __name__ == "__main__":
    main()
