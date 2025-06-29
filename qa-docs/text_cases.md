# ✅ Test Cases: Login Page (Node.js + HTML)

| TC_ID  | Title                 | Steps                                                                 | Expected Result                  |
|--------|-----------------------|------------------------------------------------------------------------|----------------------------------|
| TC_001 | Valid login           | Open login page → Enter valid email/password → Click login            | User redirected to index.html   |
| TC_002 | Invalid password      | Enter valid email + wrong password → Click login                      | Error message shown              |
| TC_003 | Empty email field     | Leave email empty → Fill password → Click login                       | Show required field error        |
| TC_004 | Empty password field  | Fill email → Leave password empty → Click login                       | Show required field error        |
| TC_005 | Server down           | Try login while backend is off                                        | Show "Error: Failed to fetch"    |
| TC_006 | SQL/script injection  | Enter "admin' OR '1'='1" in email → Click login                        | Reject with error                |
