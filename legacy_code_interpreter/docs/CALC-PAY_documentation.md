# Module: CALC-PAY.cbl

## Overview
The `CALC-PAY` module is the core computational engine of the Payroll System. It accepts raw employee time data and current salary master data to compute the Net Pay, Tax Deductions, and Social Security contributions.

## Interface Specifications
**Input (Linkage Section):**
- `LNK-EMP-ID` (PIC 9(09)): Employee Unique Identifier.
- `LNK-GROSS-SALARY` (PIC 9(07)V99): Monthly Gross Income.
- `LNK-DEPENDENTS` (PIC 9(02)): Number of dependents for tax deduction.

**Output:**
- `LNK-NET-PAY` (PIC 9(07)V99): Final amount to be transferred.
- `LNK-TAX-AMT` (PIC 9(05)V99): Calculated Income Tax.
- `LNK-RETURN-CODE` (PIC 9(02)): 00=Success, 99=Error.

## Logic Flow Summary
1. **Validation:** Checks if `GROSS-SALARY` is numeric and positive.
2. **Bracket Lookup:** Iterates through `TAX-TABLE-01` (hardcoded).
3. **Calculation:** Applies `(GROSS * RATE) - DEDUCTION`.
4. **Exception Handling:** If salary > 9,999,999.99, sets `LNK-RETURN-CODE` to 99.

---

# File: /docs/MASTER-UPD_documentation.md

# Module: MASTER-UPD.cbl

## Overview
This batch program performs the nightly synchronization of the Employee Master VSAM file. It follows the standard "Balance Line Algorithm".

## File Operations
- **Input:** `OLD-MASTER` (Sorted by ID), `TRANS-FILE` (Sorted by ID).
- **Output:** `NEW-MASTER` (Updated dataset), `ERROR-REPORT` (Text file).

## Key Logic
- **Matching:** Compares keys from both files.
  - `Key(Trans) = Key(Old)`: Update record.
  - `Key(Trans) < Key(Old)`: Add new record.
  - `Key(Trans) > Key(Old)`: Copy old record to new master (no change).
- **Deletion:** Logical deletion happens if Transaction Code = 'D'.


if __name__ == '__main__':
    unittest.main()
