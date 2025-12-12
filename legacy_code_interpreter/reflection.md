# Reflection: AI’s Role in Understanding Legacy Systems

## Introduction
Modernizing legacy systems is frequently compared to software archaeology. In our analysis of the "Legacy Payroll System" (PAYROLL-MAIN), we utilized Generative AI not merely as a coding assistant, but as a specialized translator and pattern recognizer. This reflection analyzes the efficacy of AI in navigating the complexities of 25-year-old COBOL code, highlighting where it accelerated our understanding and where human oversight remained indispensable.

## Where AI Explanations Helped Most
The most significant value add was the AI's ability to reduce cognitive load through **syntactic decryption**.
1.  **Untangling Control Flow:** In the `CALC-PAY.cbl` module, the logic relied heavily on `GO TO` statements, creating a non-linear flow that is notoriously difficult for modern developers to visualize. The AI successfully traced these execution paths, summarizing the intent of complex "spaghetti code" into clear, functional descriptions like "Tax Bracket Calculation Loop."
2.  **Bridging the Knowledge Gap:** For a team accustomed to Java or Python, mainframe terminology can be alienating. The AI effectively translated specific concepts—such as VSAM file handling, JCL job steps, and `PIC` clauses—into modern relational database or object-oriented equivalents, drastically speeding up the onboarding process.
3.  **Boilerplate Acceleration:** The generation of standard unit test structures and documentation templates (as seen in List 5) was instantaneous, allowing the engineering team to focus on edge cases rather than setup.

## Where AI Struggled
Despite its speed, the AI demonstrated limitations regarding **context and physical constraints**.
1.  **Missing Business Context:** While the AI correctly identified the mechanism of the date windowing logic (the "50" year pivot), it could not explain the historical business decision behind it. It recognized the *how*, but lacked the organizational *why* that often resides in offline meeting notes or the minds of retired staff.
2.  **Memory Layout Nuances:** In its modernization suggestions, the AI initially treated COBOL variables as independent entities. It struggled to fully grasp the risks of `REDEFINES` clauses in Copybooks, where changing a variable in one program could corrupt memory in another due to shared storage layouts—a nuance that required human intervention to prevent regression.

## Influence on Modernization Strategy
The AI-driven risk assessment fundamentally altered our roadmap. Initially, we considered a UI-first approach. However, the AI highlighted that the core business rules in `CALC-PAY` were high-risk and tightly coupled. This insight pushed us toward the **Strangler Fig pattern**. We decided to freeze the legacy code and wrap it with a Python/Java testing harness to build a "Golden Dataset" of inputs and outputs. This allows us to migrate logic piece-by-piece with confidence, rather than attempting a risky "Big Bang" rewrite.

## Lessons for Future Projects
1.  **Verify Critical Logic:** AI is excellent for summarization but can hallucinate specific math or logic flows. Financial algorithms must always be peer-reviewed against the source.
2.  **Documentation as Code:** Static documentation dies quickly. Using AI to regenerate documentation during the refactoring process ensures it remains a "living" artifact.
3.  **Test First, Refactor Later:** The greatest use of AI is generating test scenarios to map the "Black Box" behavior before changing a single line of legacy code.

## Conclusion
AI acts as a powerful force multiplier in legacy modernization. It turns opaque "black box" systems into transparent "glass boxes," enabling teams to plan migrations based on data rather than intuition. However, it requires the guidance of experienced engineers to navigate the architectural nuances that AI cannot yet fully comprehend.
