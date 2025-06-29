# 🐞 Bug Report: Login Page

**Bug Title:** Login fails silently when server is offline

**Module:** Login page (`login.html`)

**Steps to Reproduce:**
1. Stop backend server (`Ctrl+C`)
2. Open login page
3. Enter valid email and password
4. Click Login

**Expected Result:** Show a clear message like "Server not reachable"

**Actual Result:** Shows generic alert: "Error: Failed to fetch"

**Severity:** Medium  
**Priority:** High

**Suggested Fix:** Add user-friendly error handling for server/network errors.
