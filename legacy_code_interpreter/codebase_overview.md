# Codebase Overview - Legacy Payroll System (PAYROLL-MAIN)

## Age
Initial development started in 1998. The last significant compliance update was applied in 2015. Minor patches applied quarterly.

## Size
~120,000 LOC (Lines of Code) in COBOL.
~5,000 lines of JCL (Job Control Language).

## Main Dependencies
- IBM Enterprise COBOL for z/OS
- VSAM (Virtual Storage Access Method) for data storage (Employee Master File)
- CICS (Customer Information Control System) for online transaction processing
- Copybooks for shared data structures (e.g., TAX-TABLES, EMP-RECORD)

## Known Issues or Pain Points
- **Monolithic Structure:** The main calculation logic is contained in a single program (`CALC-PAY.cbl`) with over 15,000 lines.
- **Hardcoded Values:** Tax rates and thresholds from previous years are hardcoded in older subroutines rather than pulled from external tables.
- **Variable Naming:** Heavy use of non-descriptive abbreviations (e.g., `WS-AMT-1`, `WS-X`, `WS-FLAG-99`).
- **GO TO Statements:** Spaghetti code resulting from excessive use of `GO TO` statements for flow control, making logic tracing difficult.
- **Documentation:** Inline comments are sparse or obsolete; external documentation has not been updated since 2010.
