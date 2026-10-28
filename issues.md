
# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Description | Fix Approach |
|---|---|---|---|
| Mutable default argument | Bug | A shared list can retain data between calls. | Used `None` as the default and initialized a new list inside the function. |
| Hard-coded admin password | Security | A password stored in source code can be exposed. | Read the password from the `HELPDESK_ADMIN_PASSWORD` environment variable. |
| Unsafe shell execution | Security | Shell commands with user-controlled input can create injection risks. | Removed the optional ping function and its subprocess usage. |
| Invalid urgency | Input validation | Invalid urgency values can create incorrect tickets. | Validated that urgency is an integer from 1 to 5. |
| Missing ticket handling | Bug | Operations on nonexistent ticket IDs can fail. | Checked ticket existence before assigning, adding notes, or closing tickets. |
| Unsafe file handling | Code quality | Files may remain open without a context manager. | Used `with open()` and specified UTF-8 encoding. |
| Code formatting | Style | Long lines and inconsistent formatting violate Python style guidelines. | Corrected the long line and verified with Flake8. |

## Verification

- Pylint: 10.00/10 after fixes.
- Bandit: No issues identified after fixes.
- Flake8: No issues identified after fixes.
