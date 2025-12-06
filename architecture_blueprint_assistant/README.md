# Architecture Blueprint – TechEvent Hub

## Project Overview

**TechEvent Hub** is a comprehensive event management platform designed specifically for the technical community, facilitating large-scale conferences, hackathons, and workshops. The application aims to bridge the gap between complex logistical requirements and a seamless user experience for attendees, speakers, and sponsors.

The core value proposition of TechEvent Hub lies in its ability to handle high-pressure moments—such as "sold-out" ticket launches—while providing continuous engagement through real-time schedules and AI-driven networking.

**Key Documentation:**
- [Application Concept](./app_concept.md)
- [Data Model Diagram](./data_model.mmd) & [Description](./data_model.md)

---

## Architectural Evolution

Throughout this design process, we explored two distinct architectural patterns to address the system's requirements.

### 1. The Monolithic Approach
Initially, we designed a **Monolithic Architecture** where all modules (Ticketing, Networking, Schedule) resided within a single deployable unit.
- **Pros:** Simpler initial deployment and easier data consistency implementation.
- **Cons:** High risk of system-wide failure during traffic spikes. If the "Ticketing" module overloads the CPU, the "Schedule" view also goes down.
- **Artifacts:** [Diagram](./monolith_architecture.mmd) | [Description](./monolith_description.md)

### 2. The Microservices Approach
Subsequently, we decomposed the system into a **Microservices Architecture**. This design separates concerns into distinct services like *Identity*, *Ticketing*, *Payment*, and *Sponsor*.
- **Pros:** Granular scalability. We can run 50 instances of the Ticketing service during sales while keeping the Sponsor service at 2 instances. Fault tolerance is significantly improved; a crash in the "Networking" feature does not stop a user from buying a ticket.
- **Artifacts:** [Diagram](./microservices_architecture.mmd) | [Description](./microservices_description.md)

---

## Comparative Insights

The decision process involved a detailed trade-off analysis. While the Monolith offers simplicity (lower DevOps tax), the **Microservices architecture was selected as the winner**.

The deciding factor was the **Scalability Constraint**. TechEvent Hub must support up to 50k concurrent requests during ticket drops. In a monolith, scaling to this level requires replicating the entire application stack, which is resource-inefficient. Microservices allow us to scale only the bottleneck (the Ticketing Service) while maintaining cost efficiency elsewhere. Additionally, the ability to use different technologies (Polyglot) allows us to use Python for the AI Matchmaker and Go/Java for the high-performance Ticketing engine.

For a full breakdown of the trade-offs, refer to the [Architecture Comparison](./architecture_comparison.md).

---

## Data Strategy

The data model was designed to support the decoupling of services. While the logical view presents a connected web of entities (Users, Orders, Tickets, Events), the physical implementation in Microservices implies that these entities may reside in separate databases (e.g., a Relational DB for Orders, a Graph DB for Networking connections).

Key entities include:
- **Event & Session:** The core content catalog.
- **Ticket_Issued:** The digital asset requiring strong consistency and validation logic.
- **Order:** The financial record linking Users to Tickets.

---

## Lessons on AI Contribution

Using an AI assistant to generate this architectural blueprint offered several distinct advantages and learning moments:

1.  **Accelerated Boilerplating:** The AI significantly reduced the time required to generate complex MermaidJS syntax. What usually takes minutes of consulting documentation was generated instantly, allowing the architect to focus on logic rather than syntax.
2.  **Pattern Recognition:** The AI effectively applied standard industry patterns (e.g., API Gateway pattern, Event-Driven messaging) without needing explicit prompts for every detail, acting as a knowledgeable "pair programmer."
3.  **Objective Comparison:** The AI provided a neutral, fact-based comparison between architectures. It stripped away emotional bias (e.g., "I like microservices because they are trendy") and focused on engineering constraints like fault tolerance and deployment complexity.
4.  **Iterative Refinement:** The process demonstrated that AI works best with structured, iterative instructions. Breaking the task into 6 lists allowed for a higher quality output than asking for the entire blueprint in a single prompt.

In conclusion, while the AI handled the execution and formatting heavily, the human role remained critical in defining the *constraints* (50k users, GDPR compliance) that guided the architectural decisions.
