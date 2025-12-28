# data_model.md

## Entity 1: ExtractionSession
Represents a single attempt to process a URL. This is the root entity for a user action.

| Field | Type | Description |
|---|---|---|
| `session_id` | UUID (String) | Unique identifier for the generation event. |
| `source_url` | String | The URL provided by the user. |
| `timestamp` | ISO 8601 String | When the extraction occurred. |
| `raw_text_preview` | String | The first 200 chars of extracted text (for list view). |
| `selected_tone` | String | The persona used (e.g., "Mentor", "Tech Lead"). |

## Entity 2: GeneratedContent
Represents the specific output for a social platform. One Session has many GeneratedContents.

| Field | Type | Description |
|---|---|---|
| `content_id` | UUID (String) | Unique identifier for the specific post. |
| `session_id` | UUID (String) | Foreign Key linking to the ExtractionSession. |
| `platform` | Enum | "LinkedIn", "Discord", "Twitter". |
| `body_text` | String | The actual generated content (markdown supported). |
| `metadata` | Dictionary | Extra info (e.g., suggested hashtags, character count). |

## Entity 3: AppSettings
Stores local user configuration (non-sensitive or semi-sensitive data).

| Field | Type | Description |
|---|---|---|
| `setting_key` | String | Primary Key (e.g., "last_used_tone"). |
| `setting_value` | String/Any | The value of the setting. |
| `is_encrypted` | Boolean | Flag to indicate if the value needs handling (e.g., API Key). |

## JSON Schema Structure (Storage format)
Since we are using `history.json`, the data will be nested as follows:

```json
[
  {
    "session_id": "550e8400-e29b...",
    "source_url": "[https://docs.python.org/3/library/gc.html](https://docs.python.org/3/library/gc.html)",
    "timestamp": "2025-12-28T10:00:00Z",
    "selected_tone": "Technical",
    "outputs": [
      {
        "platform": "LinkedIn",
        "body_text": "Did you know Python's Garbage Collector..."
      },
      {
        "platform": "Discord",
        "body_text": "**Python Tip:** `gc.disable()` can speed up..."
      }
    ]
  }
]
