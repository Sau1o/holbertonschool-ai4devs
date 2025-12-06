# Microservices Architecture Description – TechEvent Hub

In this architecture, the application is decomposed into loosely coupled services, each with its own database, communicating via REST/gRPC and asynchronous messaging.

## Services

- **API Gateway**: The single entry point for all clients. It handles routing, rate limiting, request validation, and SSL termination.
- **Identity Service**: Responsible for user registration, authentication, and authorization (issuing JWTs). It manages user profile data securely.
- **Event Catalog Service**: Manages the core domain data: schedules, speaker profiles, room allocations, and session details.
- **Ticketing Service**: Handles ticket inventory, reservation logic, and order creation. It ensures concurrency control during high-demand sales.
- **Payment Service**: An isolated service dedicated to processing financial transactions. It interfaces with external gateways (Stripe/PayPal) to ensure PCI compliance and data security.
- **Networking Service**: Uses algorithms to suggest connections between attendees based on interests. It may utilize a Graph Database for efficient relationship mapping.
- **Sponsor Service**: Manages digital booths, sponsor assets, and lead collection analytics.
- **Notification Service**: A consumer service that listens to events (e.g., "PaymentSuccessful", "SessionChanged") from the Message Broker and sends emails or push notifications to users.
