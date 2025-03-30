#Acho-Ihim Chidera, s4  TCN-2501 
#Teacher- Mr Ikem Micheal Uche
#TCN-2501.s4.xe105.py
import os
import re
import subprocess

# Ensure the script runs with sudo
if os.geteuid() != 0:
    print("This script requires sudo privileges. Please enter your password.")
    subprocess.run(["sudo", "python3"] + os.sys.argv)
    exit()

# Path to the authentication log file
log_file = "/var/log/auth.log"

# Function to extract timestamp in ISO 8601 format from each log line
def extract_timestamp(line):
    match = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[+-]\d{2}:\d{2})?", line)
    return f"[TIMESTAMP] {match.group(0)}" if match else "[TIMESTAMP] No Timestamp"

# Open and read the log file line by line
with open(log_file, "r") as file:
    for line in file:
        timestamp = extract_timestamp(line)  # Extract timestamp from the log entry

        # Check for user creation events
        if "useradd" in line:
            print(f"{timestamp} [NEW USER] {line.strip()}")

        # Check for user deletion events
        elif "userdel" in line:
            print(f"{timestamp} [USER DELETED] {line.strip()}")

        # Check for password change events
        elif "passwd" in line and "password changed" in line.lower():
            print(f"{timestamp} [PASSWORD CHANGED] {line.strip()}")

        # Check for users switching accounts using 'su' command
        elif "su" in line:
            print(f"{timestamp} [SU COMMAND USED] {line.strip()}")

        # Detect successful 'sudo' command execution
        elif "sudo:" in line and "COMMAND=" in line:
            print(f"{timestamp} [SUDO USED] {line.strip()}")

        # Detect failed 'sudo' attempts (incorrect password or authentication failure)
        elif "sudo" in line and ("authentication failure" in line.lower() or "incorrect password" in line.lower()):
            print(f"{timestamp} [ALERT!] Failed sudo attempt! {line.strip()}")
