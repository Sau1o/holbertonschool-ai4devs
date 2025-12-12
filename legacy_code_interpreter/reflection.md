# Reflection: AI’s Role in Understanding Legacy Systems

## Introduction
Modernizing legacy systems is like software archaeology. In analyzing the "Legacy Payroll System" (PAYROLL-MAIN), we utilized Generative AI as a specialized translator and pattern recognizer. This reflection analyzes AI's efficacy in navigating 25-year-old COBOL code, highlighting where it accelerated understanding and where human oversight was indispensable.

## Where AI Explanations Helped Most
The AI’s greatest value was reducing cognitive load through **syntactic decryption**.
1.  **Untangling Control Flow:** The `CALC-PAY.cbl` module relied on non-linear `GO TO` logic. The AI successfully traced these execution paths, summarizing "spaghetti code" into clear functional descriptions like "Tax Bracket Loop," saving hours of manual mapping.
2.  **Bridging Knowledge Gaps:** It translated mainframe terms (VSAM, JCL, `PIC`) into concepts accessible to modern developers (like SQL tables or Objects), drastically speeding up the onboarding process.
3.  **Boilerplate Acceleration:** Generating standard unit test structures and documentation templates (List 5) was instantaneous, allowing the engineering team to focus on edge cases rather than setup.

## Where AI Struggled
AI demonstrated limitations regarding **context and physical constraints**.
1.  **Missing Business Context:** While AI identified the date windowing mechanism (the "50" year pivot), it missed the historical business decision behind it. It recognized *how* the code worked, but lacked the organizational *why* found in offline records.
2.  **Memory Layout Nuances:** The AI initially treated COBOL variables as independent. It struggled with `REDEFINES` clauses in Copybooks, where changing a variable in one program creates shared memory risks in another—a nuance requiring human intervention.

## Influence on Modernization Strategy
The AI-driven risk assessment shifted our roadmap from a UI-first approach to the **Strangler Fig pattern**. It highlighted that `CALC-PAY` business rules were high-risk and tightly coupled. We decided to freeze the legacy code and build a "Golden Dataset" of inputs/outputs using Python. This allows piece-by-piece migration with data-backed confidence rather than attempting a risky "Big Bang" rewrite.

## Lessons for Using AI
1.  **Verify Critical Logic:** AI summarizes well but can hallucinate math. Financial algorithms must always be peer-reviewed against the source.
2.  **Documentation as Code:** Use AI to regenerate documentation during refactoring to keep it as a "living" artifact.
3.  **Test First:** Use AI to generate test scenarios mapping "Black Box" behavior before changing any code.

## Conclusion
AI acts as a force multiplier, turning opaque "black box" systems into transparent ones. However, it requires experienced engineering guidance to navigate architectural nuances AI cannot yet fully comprehend.
