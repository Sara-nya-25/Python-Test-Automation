## Prime Number Algorithms & Test Automation
This project implements a set of prime number algorithms with a focus on 
Performance Benchmarking, Unit Testing, and Code Quality (Linting).

### 🚀 Project Overview
The goal of this project is to provide an efficient way to check for 
primality and generate lists of prime numbers while maintaining high software engineering standards.

### 📁 Structure
- src/algorithms/: Contains the core logic for prime number detection.

- tests/unit/: Standard unit tests for functional correctness using pytest.

- tests/performance/: Manual and plugin-based timing tests to measure algorithm efficiency.

- .pylintrc: Configuration for code quality standards.

- pytest.ini: Configuration for test discovery and path management.

### 🛠 Installation & Setup

1. Environment: Ensure you are using Python 3.10+ (Current environment: 3.14).

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt
   ```

### Running Tests
To run all tests and see output (including performance timing):
    ```bash
    pytest -rA or pytest -s
    ```
To run only unit tests:
    ```bash
    pytest -v -m "unit"
    ```

### 🧹 Linting & Quality
We use pylint to ensure the code follows PEP 8 standards. 
The current project maintains a 10/10 score.
    ```bash
    pylint src/ tests/
    ```