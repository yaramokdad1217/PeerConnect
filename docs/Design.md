## 🧩 Design Phase (Sprint 1 – Authentication Module)

### 🎯 Use Case Diagram

---
![PeerConnect Use Case Diagram](usecasediagram.png)

#### 🧠 Code

```plantuml
@startuml
left to right direction
skinparam actorStyle awesome
skinparam usecase {
  BackgroundColor LightBlue
  BorderColor DarkBlue
  FontSize 12
  FontColor Black
}

actor "Student" as student

rectangle "PeerConnect" {
    usecase "Register Account" as UC1
    usecase "Login" as UC2
    usecase "Validate Credentials" as UC3
    usecase "View Dashboard" as UC4
}

' Relationships
student --> UC1 : registers
student --> UC2 : logs in

UC2 --> UC3 : <<include>>
UC3 --> UC4 : <<include>>
UC1 --> UC2 : <<extend>>

@enduml
```
---

### 🎯 Class Diagram

---
![PeerConnect Use Case Diagram](classdiagram.png)

#### 🧠 Code

```plantuml
@startuml
' Simple and clear style
skinparam classAttributeIconSize 0
skinparam roundcorner 10
skinparam shadowing false
skinparam classFontName Arial
skinparam classFontSize 12

' Classes
class Student {
    - studentId: String
    - name: String
    - email: String
    - password: String
    + register()
    + login()
}

class AuthController {
    + handleRegistration()
    + handleLogin()
    + validateCredentials()
}

class UserService {
    + saveUser(user: Student)
    + getUserByEmail(email: String): Student
}

class Database {
    + storeData(data: Object)
    + retrieveData(query: Object): Object
}

' Relationships
Student --> AuthController : interacts
AuthController --> UserService : uses
UserService --> Database : connects to

@enduml
```
---

### 🎯 Sequence Diagram Flow 1: User Registration

---
![PeerConnect Sequence Diagram Flow 1](Sequencediagramflow1.png)

#### 🧠 Code
```plantuml
@startuml
actor Student
participant "UI (Registration Form)" as UI
participant AuthController
participant UserService
database Database

== User Registration Flow ==

Student -> UI : Enter name, email, password
activate UI

UI -> AuthController : sendRegistrationData(name, email, password)
activate AuthController

AuthController -> UserService : saveUser(name, email, password)
activate UserService

UserService -> Database : storeData(user)
activate Database
Database --> UserService : registrationSuccess
deactivate Database

UserService --> AuthController : userSavedConfirmation
deactivate UserService

AuthController --> UI : registrationSuccessResponse
deactivate AuthController

UI --> Student : Display success message
deactivate UI

@enduml
```
---
### 🎯 Sequence Diagram Flow 2: User Login

---
![PeerConnect Sequence Diagram Flow 1](Sequencediagramflow2.png)

#### 🧠 Code
```plantuml
@startuml
actor Student
participant "UI (Login Form)" as UI
participant AuthController
participant UserService
database Database

== User Login Flow ==

Student -> UI : Enter email, password
activate UI

UI -> AuthController : sendLoginCredentials(email, password)
activate AuthController

AuthController -> UserService : getUserByEmail(email)
activate UserService

UserService -> Database : retrieveData(email)
activate Database
Database --> UserService : userRecord
deactivate Database

UserService --> AuthController : returnUserRecord(user)
deactivate UserService

AuthController -> AuthController : validateCredentials(password, user.password)
alt Valid Credentials
    AuthController --> UI : loginSuccess()
    UI --> Student : Navigate to Dashboard
else Invalid Credentials
    AuthController --> UI : loginFailed("Invalid email or password")
    UI --> Student : Display error message
end
deactivate AuthController
deactivate UI

@enduml

```
---
