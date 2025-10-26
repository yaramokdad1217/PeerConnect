# 🎓 PeerConnect

**PeerConnect** is a web and mobile platform that helps **university students** connect with classmates for **study sessions, group projects, or peer tutoring**.  
This repository contains the **FastAPI backend** implementation for the app’s **authentication module (User Registration & Login)** — developed as part of an Agile, AI-assisted student project.

---

## 🧭 Overview

PeerConnect enables students to:
- Register securely with name, email, and password  
- Log in and authenticate to access future features  
- Form study groups, find peers by topic, and collaborate (upcoming modules)  
Future versions will integrate peer search, messaging, and skill tagging.

---

## 📁 Repository Structure


PeerConnect/
├── app/                   
│   ├── auth/
│   │   ├── controller.py        # FastAPI endpoints for registration and login
│   │   ├── service.py           # Handles core logic (register, login, password hashing)
│   │   └── models.py            # Pydantic models for requests/responses
│   └── main.py                  # Main FastAPI entry point, mounts auth routes
│   │
│   ├── tests/
│   ├── test_service.py          # Unit tests for service logic
│   └── test_controller.py       # Integration tests for API routes
│
├── docs/
    ├── project_proposal.md              # Project proposal and initial sprint goals
    ├── Design.md                        # UML and design documentation
    ├── Refactor & optimization report.md # Refactoring summary and metrics
    ├── Documentation & User Guide.md    # App usage and instructions
    ├── AI usage log.md                  # Prompts and AI reflection
    ├── classdiagram.png                 # UML class diagram
    ├── usecasediagram.png               # UML use-case diagram
    ├── Componentdiagram.png             # Deployment component diagram
    ├── Sequencediagramflow1.png         # Sequence diagram: registration
    └── Sequencediagramflow2.png         # Sequence diagram: login


