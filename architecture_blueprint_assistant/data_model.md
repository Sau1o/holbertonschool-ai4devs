# Data Model Documentation – TechEvent Hub

This document defines the core entities and attributes required for the event management system.

## Entities

- **USER**: Represents any actor in the system.
  - `id`: Unique identifier (UUID).
  - `role`: Distinguishes between Attendees, Organizers, and Admins.
  - `email`: Used for authentication and communication.

- **EVENT**: The core aggregate root for the conference context.
  - `organizer_id`: logical reference to the User who owns the event.
  - `start_date/end_date`: Defines the event duration.

- **SESSION**: Represents talks, workshops, or breaks within an event.
  - `event_id`: Links the session to a specific event.
  - `speaker_id`: Reference to the speaker profile (could be a specialized User or separate entity).

- **TICKET_TYPE**: Defines the inventory and configuration of tickets available for sale.
  - `category_name`: E.g., "Early Bird", "VIP".
  - `available_quantity`: Critical field for concurrency control during sales.

- **ORDER**: Represents a financial transaction.
  - `status`: Tracks the lifecycle of the payment (Pending -> Paid).
  - `payment_reference`: ID returned by the external payment gateway (Stripe/PayPal).

- **TICKET_ISSUED**: The actual digital asset owned by the user after purchase.
  - `qr_code_data`: Encrypted string used for check-in validation.
  - `is_checked_in`: Boolean flag to prevent double entry.
