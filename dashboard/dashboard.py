import re
from collections import Counter
import matplotlib.pyplot as plt

LOG_FILE = "../logs/cowrie.log"

source_ips = []
usernames = []

with open(LOG_FILE, "r", errors="ignore") as log:
    for line in log:

        # Capture source IPs
        ip = re.search(r'New connection: ([0-9.]+)', line)
        if ip:
            source_ips.append(ip.group(1))

        # Capture usernames
        user = re.search(r'login attempt \[(.*?)\/', line)
        if user:
            usernames.append(user.group(1))

ip_counter = Counter(source_ips)
user_counter = Counter(usernames)

# ----------------------------
# Top Source IPs
# ----------------------------

if ip_counter:

    plt.figure(figsize=(8,5))

    plt.bar(ip_counter.keys(), ip_counter.values())

    plt.title("Top Source IP Addresses")

    plt.xlabel("IP Address")

    plt.ylabel("Connections")

    plt.xticks(rotation=25)

    plt.tight_layout()

    plt.savefig("top_ips.png")

    plt.close()

# ----------------------------
# Username Attempts
# ----------------------------

if user_counter:

    plt.figure(figsize=(8,5))

    plt.bar(user_counter.keys(), user_counter.values())

    plt.title("Most Targeted Usernames")

    plt.xlabel("Username")

    plt.ylabel("Attempts")

    plt.tight_layout()

    plt.savefig("usernames.png")

    plt.close()

print("Dashboard created successfully.")