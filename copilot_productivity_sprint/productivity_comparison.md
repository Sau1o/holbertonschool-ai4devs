# Productivity Comparison Report

## Overview
This report quantifies the productivity impact of using an AI coding assistant (GitHub Copilot) versus manual coding. The data is derived from three benchmark tasks: Log Parsing (Python), User Component (React), and Data Analysis (SQL).

## Comparative Metrics Table

| Metric | Without AI (Baseline) | With AI (Copilot) | Difference |
| :--- | :--- | :--- | :--- |
| **Avg Completion Time (min)** | 18.0 min | 3.6 min | **-80%** |
| **Total Lines of Code (LOC)** | 98 lines | 75 lines | **-23%** |
| **Bugs / Test Failures** | 2 | 0 | **-100%** |

## Detailed Analysis by Metric

### 1. Completion Time (Efficiency)
* **Result:** The AI workflow was roughly 5 times faster.
* **Insight:** The greatest time reduction occurred in the SQL and Regex tasks, where the AI eliminated the need to consult external documentation (StackOverflow/Docs) for syntax verification.

### 2. Lines of Code (Conciseness)
* **Result:** AI-generated code was approximately 23% more concise.
* **Insight:**
    * *Manual:* Tended to use more verbose logic steps and extra whitespace for readability while drafting.
    * *AI:* Utilized Python list comprehensions and more compact React functional component definitions immediately.

### 3. Bugs & Quality (Accuracy)
* **Result:** Manual coding resulted in 2 initial failures, while AI code ran successfully on the first attempt.
* **Breakdown:**
    * *Manual Failures:* 1 Regex grouping error (Python) and 1 missing CSV parameter.
    * *AI Performance:* Zero syntax errors. The AI correctly predicted the need for `newline=''` in the CSV writer and correct Regex groups without prompting.
