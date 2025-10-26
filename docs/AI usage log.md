# 🤖 PeerConnect AI Usage Log

**Project:** PeerConnect  
**Author:** Yara Mokdad 
**Date:** 26-Oct-2025  

---

## Tools and Prompts

**Tools used:** ChatGPT, Microsoft Copilot  

---

### 1️⃣ Project Proposal & Requirements

**Prompt given to AI:**
> "Project Idea and Explanation: PeerConnect is a conceptual mobile and web-based application designed to help university students find classmates for group projects, study sessions, or peer tutoring."  

**AI Output Requested:**  
1. Project proposal  
   - 5 user stories  
   - Acceptance criteria  
   - Suggested priority (MoSCoW)  
   - Chosen methodology (Scrum)  
   - Sprints planning  
2. Requirements artifact  
   - Prioritized backlog  
   - Non-functional requirements  

**Notes:**  
- AI-generated output was sometimes missing acceptance criteria details or had vague priorities.  
- Follow-up prompts clarified missing details and adjusted MoSCoW priorities.  
- Final proposal and backlog were validated against beginner-friendly student project scope.  

---

### 2️⃣ Design (UML & Architecture)

**Prompt given to AI:**
> "Given the PeerConnect user stories (registration, login, peer search), produce use-case, class, and sequence diagrams for the registration/login flow using PlantUML."

**Notes:**  
- AI sometimes suggested incorrect class relationships or incomplete sequence steps.  
- Follow-up prompts fixed relationships, method calls, and sequence details.  
- Manual adjustments added deployment and component details.  
- Final diagrams were verified to match actual code logic.  

---

### 3️⃣ Implementation & Coding (Vibe Coding)

**Prompt given to AI:**
> "Generate FastAPI endpoints and Pydantic models for user registration and login, including request/response schemas and in-memory storage."

**Vibe Coding Notes:**  
- Used AI interactively in VS Code while writing code ("vibe coding") — prompting AI for small functions, testing outputs, and immediately reviewing results.  
- AI suggested boilerplate code for `controller.py`, `service.py`, and `models.py`.  
- Corrected AI outputs manually where logic or variable names did not match design.  
- Ensured password security (hashed) and consistent API responses.  
- Refined code step-by-step by asking AI follow-up questions:  
  - “Fix variable naming to be consistent with PEP8”  
  - “Return proper error codes for duplicate registration”  

**Notes on Potential AI Issues:**  
- AI initially did not handle password hashing securely.  
- Some suggested API responses were not standardized JSON.  
- Required human review and small rewrites to ensure correctness.  

---

### 4️⃣ Refactoring & Optimization

**Prompt given to AI:**
> "Analyze the authentication code for PeerConnect and suggest refactoring improvements for readability, testability, and performance."

**Notes:**  
- AI suggested splitting functions and reducing duplication.  
- Some suggestions were unnecessary or reduced clarity; manually selected the useful ones.  
- Follow-up prompts refined performance improvements and test coverage.  
- Metrics tracked:
  - Cyclomatic complexity reduced  
  - Test coverage maintained  
  - Number of lint issues reduced  

---

### 5️⃣ Testing

**Prompt given to AI:**
> "Write unit and integration tests for FastAPI registration and login endpoints, including edge cases like duplicate registration and invalid login."

**Notes:**  
- AI generated tests sometimes missed edge cases (e.g., wrong password login).  
- Follow-up prompts added missing test scenarios.  
- Verified that all tests in `test_service.py` and `test_controller.py` passed.  
- Ensured test coverage met the project requirement (≥60%).  

---

### 6️⃣ Reflection

- AI-assisted workflow followed: **Plan → Prompt → Review → Test → Document**.  
- Human review corrected errors in AI responses and ensured security, correctness, and coding standards.  
- Vibe coding allowed stepwise guidance for AI and immediate code validation.  
- Documented prompts and outputs as part of project artifacts for transparency.  
