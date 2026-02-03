
# Linux Log Analyzer (Python)

This project is a simple Python-based tool designed to analyze Linux authentication logs and identify failed login attempts that may indicate brute-force attacks or suspicious activity.

## What this project does
- Parses Linux authentication log entries (e.g. SSH failed logins)
- Extracts source IP addresses from failed login attempts
- Counts repeated failures per IP
- Generates a simple security report

## Why this matters for cybersecurity
Analyzing authentication logs is a common task in SOC and Blue Team environments. Repeated failed login attempts from the same IP may indicate brute-force or unauthorized access attempts.

## How to run
Make sure Python 3 is installed and run:

```bash
python log_analyzer.py
