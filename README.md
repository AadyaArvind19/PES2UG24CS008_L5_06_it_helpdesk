# Lab 5: Static Code Analysis — IT Helpdesk Ticket Allocator

**Course:** Software Engineering  
**Lab:** 5 — Static Code Analysis  
**Main file:** `helpdesk_system.py`

## About the Project

This project uses Python static analysis tools to improve the quality, security, and maintainability of an IT helpdesk ticket management program.

The program supports:
- Creating helpdesk tickets with urgency levels from 1 to 5.
- Assigning tickets to technicians.
- Adding notes to tickets.
- Identifying unassigned high-priority tickets.
- Closing tickets with admin password verification.
- Saving ticket data to a JSON file.

## Tools Used

- **Pylint:** Checks code quality and programming practices.
- **Bandit:** Identifies potential security vulnerabilities.
- **Flake8:** Checks Python formatting and style.

## Issues Addressed

The code was reviewed and updated to address issues including:

- Mutable default arguments.
- Hard-coded admin credentials.
- Invalid urgency values.
- Operations on nonexistent ticket IDs.
- Unsafe file handling.
- Code formatting violations.

The optional ping functionality using `subprocess` was removed to eliminate the associated Bandit findings.

## Analysis Reports

The repository contains the original and final reports for all three tools:

| Tool | Before report | After report |
|---|---|---|
| Pylint | `pylint_before.txt` | `pylint_after.txt` |
| Bandit | `bandit_before.txt` | `bandit_after.txt` |
| Flake8 | `flake8_before.txt` | `flake8_after.txt` |

### Final Results

- **Pylint:** 10.00/10
- **Bandit:** No issues identified
- **Flake8:** Verify the final report after the last formatting correction.

## Documentation

- `issues.md` — Documents identified issues and their fixes.
- `reflection.md` — Contains reflections on static code analysis.
- `.gitignore` — Excludes the virtual environment and Python cache files.

## Setup and Execution

Create and activate a virtual environment on Windows:

```cmd
python -m venv venv
venv\Scripts\activate
```

Install the analysis tools:

```cmd
python -m pip install pylint bandit flake8
```

Configure the admin password for the current Command Prompt session:

```cmd
set HELPDESK_ADMIN_PASSWORD=your_password
```

Run the program:

```cmd
python helpdesk_system.py
```

## Run Static Analysis

Generate reports using:

```cmd
python -m pylint helpdesk_system.py > pylint_after.txt 2>&1
python -m bandit -r helpdesk_system.py > bandit_after.txt 2>&1
python -m flake8 helpdesk_system.py > flake8_after.txt 2>&1
```

These commands overwrite the existing after reports. The before reports are retained for comparison.

## Conclusion

This lab demonstrates how static analysis tools can identify programming, security, and style issues without executing the source code. Applying the recommended fixes improves code quality and helps make the program safer and easier to maintain.
