# Benchmark Tasks

This document defines a set of coding tasks designed to benchmark development skills. Each task should take approximately 15-30 minutes to complete.

---

## Task 1 - CRUD Endpoint

**Requirements**: Implement a POST /users endpoint with validation for creating new users.

**Inputs**: 
- JSON payload with the following fields:
  ```json
  {
    "name": "string (required, 2-50 characters)",
    "email": "string (required, valid email format)"
  }
  ```

**Outputs**:
- On success: JSON response with the created user including a generated ID
  ```json
  {
    "id": "generated-uuid",
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```
- On error: Appropriate error message with details

**Acceptance Criteria**:
- Returns 201 status code on successful user creation
- Returns 400 status code on invalid email format
- Returns 400 status code if name is missing or outside 2-50 character range
- Returns 400 status code if email is missing
- Validates email format using regex or validation library
- Generates a unique ID for each user
- Stores user in memory or database

---

## Task 2 - Data Transformation Pipeline

**Requirements**: Implement a function that transforms an array of user objects by filtering, mapping, and aggregating data.

**Inputs**:
- Array of user objects:
  ```json
  [
    {
      "id": 1,
      "name": "Alice",
      "age": 28,
      "department": "Engineering",
      "salary": 85000
    },
    {
      "id": 2,
      "name": "Bob",
      "age": 35,
      "department": "Sales",
      "salary": 65000
    }
  ]
  ```
- Filter criteria: department name (string)
- Minimum age threshold (number)

**Outputs**:
- Transformed object containing:
  ```json
  {
    "filtered_users": ["array of users matching criteria"],
    "average_salary": "number",
    "total_count": "number"
  }
  ```

**Acceptance Criteria**:
- Filters users by specified department (case-insensitive)
- Filters users with age greater than or equal to threshold
- Calculates average salary of filtered users
- Returns 0 for average_salary if no users match criteria
- Returns total count of filtered users
- Does not modify the original input array
- Handles edge cases (empty array, no matches)

---

## Task 3 - Rate Limiter Implementation

**Requirements**: Implement a rate limiter that restricts the number of requests a user can make within a time window.

**Inputs**:
- User identifier (string)
- Rate limit configuration:
  - max_requests: maximum number of requests allowed (number)
  - time_window: time window in seconds (number)

**Outputs**:
- Boolean indicating whether the request is allowed
- Remaining requests count
- Time until reset (in seconds)
  ```json
  {
    "allowed": true,
    "remaining": 8,
    "reset_in": 45
  }
  ```

**Acceptance Criteria**:
- Allows up to max_requests within the time_window
- Returns allowed: true when under the limit
- Returns allowed: false when limit is exceeded
- Tracks requests per user independently
- Resets counter after time_window expires
- Returns accurate remaining request count
- Returns accurate reset time in seconds
- Handles concurrent requests correctly
- Cleans up expired entries to prevent memory leaks

---

## Task 4 - Simple Search API with Pagination

**Requirements**: Implement a GET /search endpoint that searches through a collection of articles and returns paginated results.

**Inputs**:
- Query parameters:
  - `q`: search query string (required)
  - `page`: page number (optional, default: 1)
  - `limit`: results per page (optional, default: 10, max: 100)

**Outputs**:
- JSON response with search results and pagination metadata:
  ```json
  {
    "results": [
      {
        "id": 1,
        "title": "Article Title",
        "content": "Article content...",
        "relevance_score": 0.95
      }
    ],
    "pagination": {
      "current_page": 1,
      "total_pages": 5,
      "total_results": 47,
      "per_page": 10
    }
  }
  ```

**Acceptance Criteria**:
- Returns 200 status code on successful search
- Returns 400 status code if query parameter `q` is missing
- Searches through article titles and content (case-insensitive)
- Calculates relevance score based on keyword matches
- Returns results sorted by relevance score (highest first)
- Implements pagination correctly (skips appropriate records)
- Enforces maximum limit of 100 results per page
- Returns empty results array if no matches found
- Includes accurate pagination metadata
- Handles edge cases (page beyond available pages returns empty results)

---

## Task 5 - Cache Implementation with TTL

**Requirements**: Implement a simple in-memory cache with Time-To-Live (TTL) support and LRU eviction policy.

**Inputs**:
- Cache configuration:
  - `max_size`: maximum number of items (number)
  - `default_ttl`: default time-to-live in seconds (number)
- Operations:
  - `set(key, value, ttl)`: store a value
  - `get(key)`: retrieve a value
  - `delete(key)`: remove a value
  - `clear()`: remove all values

**Outputs**:
- For `get(key)`: Returns the value if exists and not expired, otherwise null/undefined
- For `set(key, value)`: Returns boolean indicating success
- For `delete(key)`: Returns boolean indicating if key existed

**Acceptance Criteria**:
- Stores key-value pairs with TTL
- Returns value for valid, non-expired keys
- Returns null/undefined for expired or non-existent keys
- Automatically removes expired entries on access
- Implements LRU eviction when max_size is reached
- Uses default_ttl when no TTL is specified for set()
- Supports custom TTL per key
- Updates access time when key is retrieved (for LRU)
- Properly cleans up expired entries
- Handles edge cases (setting same key updates value and TTL)
