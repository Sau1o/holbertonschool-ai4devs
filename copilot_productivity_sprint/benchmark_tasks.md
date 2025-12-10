# Benchmark Tasks - Copilot Productivity Sprint

This document defines the set of coding tasks used to evaluate the efficiency and accuracy of the AI coding assistant.

## Task 1: Data Processing Script (Python)
**Objective:** Create a utility script to parse a log file and extract specific error metrics.

* **Requirements:**
    * Read a text file containing server logs.
    * Identify lines containing the string "[ERROR]".
    * Extract the timestamp and the error message from these lines.
    * Count the frequency of each unique error message.
* **Inputs:**
    * A file named `server.log` containing raw log data (lines with timestamps, log levels, and messages).
* **Outputs:**
    * A CSV file named `error_summary.csv` with columns: `Error Message`, `Count`.
    * A print to console showing the most frequent error.
* **Acceptance Criteria:**
    * The script runs without syntax errors.
    * The CSV is generated correctly.
    * The script handles empty input files gracefully (prints a warning).
    * Regex is used for parsing the log lines.

## Task 2: Frontend Component (React/TypeScript)
**Objective:** Build a reusable "User Card" component that displays profile information with a toggleable "Follow" state.

* **Requirements:**
    * Create a functional React component named `UserCard`.
    * Display the user's avatar, name, and bio.
    * Include a "Follow/Unfollow" button.
    * Style the component using CSS modules or Tailwind (assume Tailwind is available).
* **Inputs:**
    * Props interface: `avatarUrl` (string), `name` (string), `bio` (string), `initialIsFollowing` (boolean).
* **Outputs:**
    * A rendered HTML structure representing the card.
    * Visual change in button style when toggled (e.g., Blue for Follow, Gray for Unfollow).
* **Acceptance Criteria:**
    * Component renders all props correctly.
    * Clicking the button toggles the internal state and the button text.
    * The component is strictly typed (no `any` types).

## Task 3: SQL Query Generation (SQL)
**Objective:** Write a complex query to analyze e-commerce sales performance by category.

* **Requirements:**
    * Join three tables: `Orders`, `OrderItems`, and `Products`.
    * Calculate the total revenue for each product category for the current year.
    * Filter out categories with less than $1,000 in total revenue.
    * Order the results by revenue in descending order.
* **Inputs:**
    * Table Schema `Orders` (id, order_date, customer_id).
    * Table Schema `OrderItems` (id, order_id, product_id, quantity, unit_price).
    * Table Schema `Products` (id, name, category, price).
* **Outputs:**
    * A result set with columns: `Category`, `TotalRevenue`, `TotalItemsSold`.
* **Acceptance Criteria:**
    * The query uses correct JOIN syntax.
    * The date filter correctly applies to the current year.
    * The `HAVING` clause is used for the revenue threshold.
    * Aggregations (`SUM`) are correct.
