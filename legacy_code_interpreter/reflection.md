# Reflection: AI’s Role in Understanding Legacy Systems

## Introduction
Modernizing legacy systems, particularly those written in COBOL from the late 90s, is often compared to archaeology. The documentation is usually missing, the original developers have retired, and the business logic is buried under layers of patches. In this context, Generative AI acts not just as a tool, but as a translator and accelerator. This reflection analyzes the experience of using AI to document, analyze, and test the "Legacy Payroll System".

## Where AI Explanations Helped Most
The greatest strength of the AI was its ability to perform **syntactic decryption** and **pattern recognition** at speed.
1.  **Decoding "Spaghetti Code":** In modules like `CALC-PAY.cbl`, where `GO TO` statements created a non-linear flow, the AI successfully traced the execution paths and summarized the intent (e.g., "Tax Bracket Logic") in plain English. Doing this manually would take a human developer hours of graph-plotting.
2.  **Jargon Translation:** The AI effortlessly translated mainframe-specific concepts (VSAM, JCL, CICS, PIC clauses) into modern terminology that a junior developer or a stakeholder could understand.
3.  **Boilerplate Generation:** Creating the initial structure for documentation and standard unit tests (List 5) was instantaneous, removing the "blank page syndrome" and allowing the team to focus on edge cases.

## Where AI Struggled
The AI showed limitations in understanding **context** and **external dependencies**:
1.  **Business "Why" vs. Code "How":** While the AI could explain *how* the date windowing logic worked (List 2), it couldn't fully explain *why* the pivot year was set to "50" without external context. It inferred it was a Y2K fix, but missed potential specific business rules that might have dictated that decision.
2.  **False Confidence in Refactoring:** In the modernization plan (List 4), the AI suggested splitting the monolith. While correct in theory, it initially underestimated the complexity of separating data that is tightly coupled in shared Copybooks. It treats code as modular text, whereas COBOL variables often overlap in memory (REDEFINES) in dangerous ways.

## How AI Influenced the Modernization Strategy
The AI's risk assessment (List 3) fundamentally shifted the strategy from a "Big Bang Rewrite" to a **Strangler Fig pattern**. By clearly identifying high-severity risks like the hardcoded tax logic and the brittle file-matching routine, the AI helped prioritize extracting the "Calculation Engine" first, rather than trying to replace the UI or the Database immediately. It highlighted that the logic was the most volatile part, dictating the roadmap order.

## Lessons for Using AI on Legacy Projects
1.  **Trust but Verify:** AI is excellent for summarization but can hallucinate variable relationships. Every explanation for critical financial code (Payroll) must be peer-reviewed against the source.
2.  **Force Multiplier for Tests:** The best use case is generating "Golden Data" test cases. We can use AI to write Python scripts that throw thousands of inputs at the COBOL code to map its behavior before we change a single line.
3.  **Documentation is Living:** AI allows us to treat documentation as code. As we refactor, we can regenerate the docs, keeping them in sync, which solves the historical problem of outdated manuals.

## Conclusion
AI does not replace the need for a seasoned Mainframe Engineer, but it dramatically lowers the barrier to entry for modernizing these systems. It turns an opaque black box into a glass box, allowing us to see the risks and plan the migration with data-backed confidence.
