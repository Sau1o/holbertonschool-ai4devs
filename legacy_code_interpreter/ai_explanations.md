# AI Explanations - Legacy Payroll System

## Section 1 – CALC-PAY.cbl :: TAX-BRACKET-LOGIC

- **Plain English**: This section calculates the employee's tax deduction based on their gross salary. It checks a series of hardcoded salary ranges (brackets). If the salary falls within a range, it applies a specific percentage and adds a fixed base amount. It repeats this check for multiple levels until the correct bracket is found.
- **Pattern**: Deeply nested `IF-ELSE` structures mixed with `GO TO` statements to jump out of the logic once a match is found.
- **Issues**:
    - "Magic numbers" (hardcoded tax rates and thresholds) make it risky to update for new tax years.
    - Cyclomatic complexity is very high due to nesting.
    - Unreachable code detected after certain `GO TO` statements.
- **Improvements**:
    - Refactor into a `EVALUATE` statement (COBOL's switch/case) or look up values from an external DB2 table or VSAM file.
    - Extract calculation logic into a separate sub-program (`TAX-CALC`).

## Section 2 – MASTER-UPD.cbl :: FILE-MATCHING-ROUTINE

- **Plain English**: This routine synchronizes two files: the `OLD-MASTER` (existing employee data) and `TRANS-FILE` (daily updates). It reads both files sequentially. It compares the Employee ID keys to decide whether to add a new record, update an existing one, or delete a record. It handles the "balance line algorithm" logic manually.
- **Pattern**: Classical sequential file processing (Old Master / Transaction -> New Master).
- **Issues**:
    - The logic for handling End-of-File (EOF) on one file while the other is still open is brittle and prone to infinite loops if the `HIGH-VALUES` logic fails.
    - Variable names like `WS-SW-EOF-1` and `WS-SW-EOF-2` are not intuitive.
- **Improvements**:
    - Migrate data to a relational database (SQL) to eliminate the need for manual sequential file matching.
    - If maintaining COBOL, use standard `PERFORM UNTIL` loops with clear termination conditions.

## Section 3 – UTILS.cbl :: DATE-CONV-YY-YYYY

- **Plain English**: A utility paragraph attempting to handle date expansion. It takes a 2-digit year input. If the year is greater than 50, it assumes the prefix "19"; otherwise, it assumes "20". It constructs a full YYYYMMDD date from a YYMMDD input.
- **Pattern**: Windowing technique for Y2K remediation.
- **Issues**:
    - Hardcoded pivot year (50) means this logic will become incorrect again in the future (specifically in 2050).
    - No validation to check if the input date is numeric or valid (e.g., handles "February 30th" incorrectly).
- **Improvements**:
    - Use COBOL intrinsic functions like `FUNCTION CURRENT-DATE` or `FUNCTION INTEGER-OF-DATE`.
    - Replace custom windowing logic with system-standard date routines.
