# 📘 **1. Project Proposal – PeerConnect**

## **Project Overview**

**PeerConnect** is a mobile and web-based platform for university students to connect with classmates for **group projects, study sessions, or peer tutoring**.
The system simplifies peer discovery and scheduling by letting users:

* Search peers by **course or topic**
* **Create/join study sessions**
* **Message group members**
* View basic **skill levels or experience**



---

## **Agile Methodology**

**Chosen Methodology:** *Scrum*

* Short development cycles called **Sprints**
* Regular review and retrospective per sprint
* Continuous incremental delivery
* Suitable for learning and iterative improvement

### **Sprint Plan (4 Sprints Total)**

| Sprint                      | Duration | Goals                                                  |
| --------------------------- | -------- | ------------------------------------------------------ |
| **Sprint 1 (Week 1)**       | 1 week   | Basic UI setup, user registration/login                |
| **Sprint 2**                | 2 weeks  | Search for peers by course/topic, view peer profiles   |
| **Sprint 3**                | 2 weeks  | Create/join study sessions, basic messaging            |
| **Sprint 4 (Final Sprint)** | 2 weeks  | Skill-level feature, UI polish, testing, documentation |

---

## **User Stories (with Acceptance Criteria & MoSCoW Priority)**

| #     | User Story                                                                                                          | Acceptance Criteria                                                                                                                                  | Priority (MoSCoW)                                |
| ----- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **1** | As a **student**, I want to **create an account and log in** so I can access PeerConnect features.                  | - User can register with name, email, and password<br>- User can log in and log out successfully<br>- Errors shown for invalid login or empty fields | **Must Have**                                    |
| **2** | As a **student**, I want to **search for peers by course or topic** so I can find people studying similar subjects. | - Search bar available<br>- Results display matching users with name, course, and small profile info<br>- No results message shown if none found     | **Must Have**                                    |
| **3** | As a **student**, I want to **create or join a study session** so I can collaborate with classmates.                | - Users can create a session (title, course, time)<br>- Other users can join an existing session<br>- Session list visible                           | **Should Have**                                  |
| **4** | As a **student**, I want to **send messages or notes to my study group** to coordinate plans.                       | - Each session has a simple message board/chat<br>- Users can post and view messages<br>- No need for real-time chat in first version                | **Could Have**                                   |
| **5** | As a **student**, I want to **see the skill levels or experience of my peers** to choose suitable teammates.        | - Each profile shows a simple skill rating (beginner/intermediate/advanced)<br>- Optional to display skill level                                     | **Won’t Have (for MVP, can be in final sprint)** |

---

# 📋 **2. Requirements Artifact**

## **2.1 Product Backlog (Prioritized)**

| Priority | Feature                        | Description                                   | Sprint     |
| -------- | ------------------------------ | --------------------------------------------- | ---------- |
| 1️⃣      | **User Authentication**        | Register, login, logout                       | Sprint 1   |
| 2️⃣      | **Search Functionality**       | Search peers by course/topic                  | Sprint 2   |
| 3️⃣      | **Profile Display**            | Show basic peer info and skill level (later)  | Sprint 2–4 |
| 4️⃣      | **Session Creation & Joining** | Create/join group study sessions              | Sprint 3   |
| 5️⃣      | **Group Messaging/Notes**      | Simple discussion board for session members   | Sprint 3   |
| 6️⃣      | **Skill Level Tagging**        | Optional peer skill tag on profile            | Sprint 4   |
| 7️⃣      | **UI Polish & Testing**        | Improve design, fix bugs, write documentation | Sprint 4   |

---

## **2.2 Non-Functional Requirements**

| Category            | Requirement                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| **Performance**     | The app should load main screens within **2 seconds** on a standard internet connection.      |
| **Usability**       | Simple navigation with 3–4 core screens (Home, Search, Sessions, Profile).                    |
| **Scalability**     | Should support at least **100 users** without performance degradation (local DB or Firebase). |
| **Reliability**     | User sessions persist until logout; handle offline gracefully where possible.                 |
| **Security**        | Passwords stored securely (hashed); authentication via Firebase/Auth library.                 |
| **Maintainability** | Code should be modular and documented to allow future feature expansion.                      |
| **Compatibility**   | Should work on **web** and **mobile** (React Native or Flutter).                              |
| **Accessibility**   | Text and buttons must be readable and properly labeled for clarity.                           |


---

**3. UML Diagrams**
https://github.com/yaramokdad1217/PeerConnect/blob/main/docs/Design.md
---

**4. UI Design**
First sketch of PeerConnect sprint 1 UI pages:[ https://www.figma.com/make/jMnICis0nyWg0H3tTVv0bi/Student-Study-Collaboration-App?node-id=0-1&p=f&t=iQtfhFFNcazPFkcy-0&fullscreen=1](https://www.figma.com/make/jCi7V6a97KbNqbxRtOXYtp/PeerConnect-Student-App-Design?node-id=0-1&p=f&t=tGDFhgIlkVTbiDCw-0&fullscreen=1)
---

