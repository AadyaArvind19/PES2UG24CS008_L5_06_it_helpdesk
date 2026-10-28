# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding-style issues.

## 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint checks code quality and programming practices. Bandit identifies common security vulnerabilities in Python code. Flake8 checks formatting and adherence to Python style guidelines.

## 3. How did static analysis improve the helpdesk program?

Static analysis helped identify problems involving mutable default arguments, hard-coded passwords, input validation, missing-ticket handling, and code formatting. Fixing these issues improved the program's security, reliability, and maintainability.

## 4. What are the limitations of static code analysis?

Static analysis cannot detect every runtime error or security vulnerability. The program must also be tested with different inputs to verify its behavior.
