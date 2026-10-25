# Automated Web Security Header Checker Using Python

## 1. Objective
To develop a simple Python tool that checks whether common HTTP security headers are present in a website's response.

## 2. Technologies Used
- Python
- Requests library
- Visual Studio Code

## 3. Methodology
The program accepts a website URL, sends an HTTP request, receives the response, and checks five security headers: Content-Security-Policy, Strict-Transport-Security, X-Content-Type-Options, X-Frame-Options, and Referrer-Policy.

It displays the HTTP status and identifies which headers are present or missing.

## 4. Result
The program was tested using https://example.com. It received HTTP status 200 and displayed the results of all five header checks.

## 5. Conclusion
The project demonstrates how Python can automate a basic website security-header check. It helps users identify missing security headers for further investigation. It is a basic assessment tool, not a complete security audit.

## 6. Future Improvements
- Save scan results to a text or CSV report.
- Add a graphical user interface.
- Check additional security headers.
