# Data Model

## Entity: User
Represents the authenticated account holder.
- **id** (UUID, PK): Unique identifier.
- **email** (String): User email for login.
- **api_key** (String): Internal key for API access.
- **created_at** (Timestamp).

## Entity: AutomationHook
Represents a target external workflow (e.g., n8n, Zapier, Make).
- **id** (UUID, PK): Unique identifier.
- **user_id** (UUID, FK): Owner of the hook.
- **name** (String): Friendly name (e.g., "Create CRM Lead").
- **description** (Text): Context for the AI to understand when to use this hook.
- **target_url** (String): The webhook endpoint URL.
- **json_schema** (JSON): The expected structure of the payload (e.g., `{"name": str, "email": str}`).

## Entity: CommandLog
Records every attempt to use the system for auditing and debugging.
- **id** (UUID, PK): Unique identifier.
- **user_id** (UUID, FK): Who executed the command.
- **hook_id** (UUID, FK, Nullable): Which hook was matched (if any).
- **raw_input** (Text): The transcribed text or typed input.
- **parsed_payload** (JSON): The data extracted by the AI.
- **status** (Enum): `SUCCESS`, `FAILED`, `NO_MATCH`.
- **latency_ms** (Integer): Time taken to process.
- **created_at** (Timestamp).
