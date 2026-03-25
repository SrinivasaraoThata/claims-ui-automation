# Requirements Traceability Matrix (RTM)

| Req ID | Business Requirement | Test Case ID | Test Case Description | Status |
|--------|----------------------|--------------|-----------------------|--------|
| **REQ-LOG-01** | Member must be able to securely login to the Portal. | TC-01 | Verify successful login with valid credentials. | **Automated** |
| **REQ-LOG-02** | Member must see an error message for invalid login credentials. | TC-02 | Verify login-failed message for invalid credentials. | **Automated** |
| **REQ-CLM-01** | Member must see their latest claim status correctly displayed. | TC-03 | Verify claim status for existing member claims. | **Automated** |
| **REQ-CLM-02** | Member must be able to search claims by status or ID. | TC-04 | Verify search and filter functionality on claims page. | **In Progress** |
| **REQ-PRF-01** | Member must be able to update their contact information safely. | TC-05 | Verify profile update reflection after modification. | **Planned** |

---

## RTM Overview
The matrix above ensures every business requirement is mapped to a specific test case within the `tests/` directory.

- **Automated**: Completed and verified in CI/CD pipeline.
- **In Progress**: Code is under development in a separate branch.
- **Planned**: Scheduled for the next sprint/test phase.
