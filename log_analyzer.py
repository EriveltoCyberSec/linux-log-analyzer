import re
from collections import Counter

LOG_DATA = """
Jan 10 10:15:32 server sshd[1234]: Failed password for invalid user admin from 192.168.1.10 port 55234 ssh2
Jan 10 10:16:01 server sshd[1235]: Failed password for root from 192.168.1.10 port 55235 ssh2
Jan 10 10:17:45 server sshd[1236]: Failed password for user from 10.0.0.5 port 44211 ssh2
Jan 10 10:18:10 server sshd[1237]: Failed password for root from 192.168.1.10 port 55236 ssh2
"""

FAILED_LOGIN_PATTERN = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

def analyze_logs(log_text):
    failed_ips = []

    for line in log_text.splitlines():
        match = FAILED_LOGIN_PATTERN.search(line)
        if match:
            failed_ips.append(match.group(1))

    return Counter(failed_ips)

def generate_report(counter):
    print("=== Security Log Analysis Report ===\n")

    if not counter:
        print("No failed login attempts found.")
        return

    for ip, attempts in counter.most_common():
        print(f"IP: {ip} | Failed attempts: {attempts}")

if __name__ == "__main__":
    result = analyze_logs(LOG_DATA)
    generate_report(result)
