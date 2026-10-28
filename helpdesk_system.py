
"""Helpdesk ticket management with input validation and security."""

import json
import os
from datetime import datetime
from itertools import count

# Global state
tickets = {}
TICKET_IDS = count(101)

# Read the admin password from an environment variable.
ADMIN_PASSWORD = os.getenv("HELPDESK_ADMIN_PASSWORD")


def raise_ticket(user, issue_type, urgency="3", audit_trail=None):
    """Create a helpdesk ticket after validating its urgency."""
    if audit_trail is None:
        audit_trail = []

    try:
        priority = int(urgency)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            "Urgency must be an integer from 1 to 5"
        ) from exc

    if not 1 <= priority <= 5:
        raise ValueError("Urgency must be between 1 and 5")

    ticket_id = next(TICKET_IDS)
    tickets[ticket_id] = {
        "user": user,
        "issue": issue_type,
        "priority": priority,
        "tech": None,
        "notes": [],
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }

    audit_trail.append(
        f"{user} raised #{ticket_id} at {datetime.now()}"
    )
    return ticket_id


def assign_ticket(ticket_id, technician):
    """Assign an existing ticket to a technician."""
    if ticket_id not in tickets:
        return False

    tickets[ticket_id]["tech"] = technician
    return True


def add_note(ticket_id, note):
    """Add a note to an existing ticket."""
    if ticket_id not in tickets:
        return False

    tickets[ticket_id]["notes"].append(note)
    return True


def close_ticket(ticket_id, password):
    """Close a ticket after validating the admin password."""
    if not ADMIN_PASSWORD or password != ADMIN_PASSWORD:
        return False

    if ticket_id not in tickets:
        return False

    del tickets[ticket_id]
    return True


def unresolved_high_priority():
    """Return unassigned tickets with priority 4 or 5."""
    return [
        ticket_id
        for ticket_id, ticket in tickets.items()
        if ticket["priority"] >= 4 and ticket["tech"] is None
    ]


def save_tickets(file="tickets.json"):
    """Save current tickets to a JSON file."""
    with open(file, "w", encoding="utf-8") as output_file:
        json.dump(tickets, output_file, indent=4)


def main():
    """Run a demonstration of the helpdesk system."""
    printer_ticket = raise_ticket("anil", "printer", "5")
    raise_ticket("meera", "wifi", "4")
    vpn_ticket = raise_ticket("joe", "vpn", "2")

    assign_ticket(printer_ticket, "Tech-Kiran")
    add_note(999, "Called user")

    print("Unassigned high priority:", unresolved_high_priority())

    urgency = (
        input(
            "Urgency for a new laptop ticket (1-5, Enter for 3): "
        ).strip()
        or "3"
    )

    try:
        raise_ticket("sana", "laptop", urgency)
    except ValueError as exc:
        print(f"Could not create laptop ticket: {exc}")

    if ADMIN_PASSWORD:
        if close_ticket(vpn_ticket, ADMIN_PASSWORD):
            print(f"Ticket #{vpn_ticket} closed.")
        else:
            print(f"Could not close ticket #{vpn_ticket}.")
    else:
        print("Admin password is not configured; ticket was not closed.")

    save_tickets()
    print("Open tickets:", list(tickets.keys()))


if __name__ == "__main__":
    main()
