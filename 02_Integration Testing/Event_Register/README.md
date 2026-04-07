# Event Registration System
A lightweight Python-based membership and event management system. This project demonstrates clean architecture by separating core logic from unit and integration tests using pytest.

## 🏗 Project Structure
The project follows a standard src/ layout to ensure clean imports and professional testing patterns.
```
Event_Register/       # Project metadata and path configuration
├── pytest.ini      # pytest markers and pytest configuration
├── conftest.py          # Root marker for path discovery
├── src/
│   └── membership.py    # Core Logic (Event & MemberService classes)
└── tests/
    ├── unit/            # Fast tests for individual methods (includes Spies)
    └── integration/     # Tests for class interactions and workflows
```

## 🚀 Getting Started
**Prerequisites**
Python 3.10+

pip

Installation
Clone the repository to your local machine.

Install the required testing dependencies:

Bash
pip install pytest pytest-mock

##🧪 Running Tests
You can run the entire suite or target specific layers of the application.

Run all tests: pytest

Run only Unit Tests: pytest tests/unit

Run only Integration Tests: pytest tests/integration

## 🛠 Features
**Core Classes**
**MemberService:** Manages the global registry of club members.

**Event:** Handles event-specific sign-ups and coordinates with the MemberService to ensure new members are registered globally during event entry.

**Testing Strategy**
**Unit Tests:** Uses mocker.spy to verify that MemberService.add_member is called correctly without breaking its internal logic.

**Integration Tests:** Verifies the "handshake" between an Event instance and the MemberService to ensure data consistency across both objects.

## 📝 Configuration
This project uses pyproject.toml to manage the Python path. This ensures that the src folder is automatically recognized by pytest, preventing ModuleNotFoundError during test execution.

