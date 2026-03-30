# Requirements Traceability Matrix (RTM)

| Requirement ID | Feature | Test Case | Complexity | Technical Notes |
|----------------|---------|-----------|------------|-----------------|
| **REQ-01** | User Auth | Login with Valid Credentials | Low | Standard POM implementation. |
| **REQ-02** | Accounts | Dashboard Data Validation | Medium | Uses Regex to scrub currency symbols before assertion. |
| **REQ-03** | Transfers | Funds Transfer Between Accounts | High | Requires "Session Health Check" to ensure login didn't drop mid-flow. |
| **REQ-04** | Services | Loan Request Submission | High | Challenge: Asynchronous success message; uses FluentWait. |
