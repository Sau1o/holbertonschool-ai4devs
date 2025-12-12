# Modernization Plan - Legacy Payroll System

## Phase 1 - Short Term: Stabilization & Observation (Months 1-3)
**Strategy:** "Freeze and Wrap"
- **Actions:**
    1.  **Automated Regression Testing:** Implement a "Record/Replay" testing harness. Capture inputs and outputs of `CALC-PAY.cbl` from the last 6 months of production runs to create a "Golden Dataset".
    2.  **AI-Assisted Documentation:** Run the codebase through an LLM to generate current functional specifications and data flow diagrams.
    3.  **Code Cleanup:** Apply automated formatting tools to standardize indentation and remove dead code (unreachable logic identified in the risk assessment).

- **Risks:** Breaking undocumented dependencies during cleanup.
- **Mitigation:** Strict code freeze on new features; only critical bug fixes allowed. Rely heavily on the Golden Dataset for verification before any commit.

## Phase 2 - Medium Term: Hybrid Architecture (Months 4-12)
**Strategy:** "Strangler Fig Pattern" & API Enablement
- **Actions:**
    1.  **Extract Business Rules:** Isolate the Tax Calculation logic (`TAX-BRACKET-LOGIC`) from the COBOL monolith.
    2.  **Microservice Implementation:** Re-implement the tax logic in a modern language (e.g., Java/Spring Boot or Python) hosted on a cloud container.
    3.  **Mainframe Bridge:** Use z/OS Connect or IBM MQ to allow the Legacy COBOL program to call the new Tax Microservice instead of the internal subroutine.

- **Risks:** Latency introduced by network calls; Data type conversion errors (EBCDIC vs. ASCII).
- **Mitigation:** Implement "Parallel Run" mode where both the old COBOL logic and new Microservice run, logging discrepancies without affecting the actual payroll result until 100% accuracy is achieved.

## Phase 3 - Long Term: Re-platforming (Year 1+)
**Strategy:** "Full Cloud Migration"
- **Actions:**
    1.  **Data Migration:** Migrate VSAM files (Employee Master) to a Relational Database (PostgreSQL) using ETL pipelines.
    2.  **UI Modernization:** Replace CICS "Green Screens" with a Web-based Dashboard (React/Angular) communicating with the new backend.
    3.  **Decommission:** Once all modules (Benefits, Time & Attendance, Reporting) are strangled out, retire the mainframe job scheduler and datasets.

- **Risks:** Loss of historical data context; Training gaps for current support staff.
- **Mitigation:** Keep read-only archival access to the mainframe for 1 year post-migration. Invest in upskilling the current COBOL maintenance team to the new tech stack.
