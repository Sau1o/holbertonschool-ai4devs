# architecture.md

## High-Level System Architecture

The system follows a monolithic script architecture suitable for Streamlit (MVP), interacting with external APIs for intelligence and the local file system for persistence.

```mermaid
graph TD
    User[User / Browser] -- HTTPS/Interaction --> UI[Streamlit Frontend]
    
    subgraph "Application Core (Python)"
        UI -- Triggers --> Controller[Logic Controller]
        Controller -- "1. Request HTML" --> Scraper[Scraper Module (BeautifulSoup/Requests)]
        Controller -- "3. Prompt Engineering" --> AI_Engine[LLM Handler]
        Controller -- "5. Read/Write" --> Storage[Local File Manager]
    end
    
    subgraph "External World"
        Scraper -- "2. Fetch Content" --> TargetURL[Target Website]
        AI_Engine -- "4. API Call" --> OpenAI[OpenAI API (GPT-4o-mini)]
    end
    
    subgraph "Data Layer"
        Storage -- JSON --> HistoryDB[(history.json)]
        Storage -- ENV --> Config[(.env / config)]
    end
