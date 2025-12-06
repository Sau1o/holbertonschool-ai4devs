# Monolithic Architecture Description – TechEvent Hub

This document outlines the monolithic architecture for the TechEvent Hub platform, where all business logic resides within a single deployable unit.

## Components

- **Client Application (Web/Mobile)**: The single-page application (SPA) and mobile app that serve as the user interface for attendees, speakers, and organizers.
- **Load Balancer**: Distributes incoming network traffic across multiple instances of the monolith to ensure reliability and handle traffic spikes during ticket sales.
- **TechEvent Monolith Server**: The core application container (e.g., Spring Boot or Node.js) that hosts all business logic and API endpoints.
- **Authentication Module**: Handles user registration, login, JWT issuance, and role-based access control (RBAC) for all user types.
- **Ticketing & Sales Module**: Manages ticket inventory, pricing tiers, discount codes, and order processing logic.
- **Schedule Management Module**: Handles the creation and modification of event agendas, speaker assignments, and room allocations.
- **Networking Module**: Contains the logic for attendee profile matching and chat functionalities.
- **Central Relational Database**: A single, large database instance (e.g., PostgreSQL) storing all data (users, orders, schedules) with foreign key relationships ensuring data integrity.
- **External Payment Gateway**: A third-party service (e.g., Stripe/PayPal) integrated via API to securely process credit card transactions.
