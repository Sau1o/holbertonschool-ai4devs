# Risk Assessment - Legacy Payroll System

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| **Hardcoded Business Logic** | **High** | Tax rates and bracket thresholds are embedded in `CALC-PAY.cbl`. Any change in labor legislation requires recompiling the source code, increasing the risk of introducing regression bugs during mandatory updates. |
| **Spaghetti Code / Control Flow** | **High** | Excessive use of `GO TO` and `PERFORM THRU` in the main logic makes the code non-linear. This drastically increases the time required to diagnose production bugs and makes refactoring nearly impossible without breaking functionality. |
| **Data Security (VSAM)** | **High** | Employee sensitive data (PII) is stored in flat VSAM files without encryption at rest. Direct access to the mainframe dataset could compromise data privacy regulations (e.g., LGPD/GDPR). |
| **Date Windowing Logic** | **Medium** | The date conversion routine uses a hardcoded pivot year (50) to interpret 2-digit years. While currently functional, this is a technical debt that will cause data corruption or calculation errors as the system approaches the year 2050. |
| **Documentation Obsolescence** | **Low** | Comments in the code refer to "new features" from 2005. External documentation is missing. While not an immediate runtime risk, it slows down onboarding of new developers significantly. |
