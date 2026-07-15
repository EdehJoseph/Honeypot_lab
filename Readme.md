# Cowrie Honeypot Dashboard Lab

## Overview

This project demonstrates the deployment of a Cowrie SSH honeypot on Kali Linux running inside VMware Fusion. The objective was to simulate a production SSH service, capture login attempts, analyze attacker behavior, and document the process using GitHub.

Cowrie is a medium interaction SSH and Telnet honeypot that records authentication attempts, commands entered by attackers, and session activity without exposing a real system.

---

## Objectives

- Deploy a Cowrie SSH honeypot
- Simulate an exposed SSH service
- Capture login attempts and commands
- Analyze generated logs
- Document findings
- Practice cybersecurity monitoring and log analysis

---

## Technologies Used

- Kali Linux
- VMware Fusion
- Cowrie Honeypot
- Python
- Git
- GitHub

---

## Project Structure

```
honeypot_dashboard_lab/
├── dashboard/
│   └── dashboard.py
├── logs/
│   └── cowrie.log
├── notes/
│   └── analysis.md
├── screenshots/
└── README.md
```

---

## Installation Process

A Kali Linux virtual machine was deployed using VMware Fusion.

The Cowrie repository was cloned from GitHub, a Python virtual environment was created, dependencies were installed, and Cowrie was configured before launching the SSH honeypot.

---

## Running the Honeypot

The honeypot was started successfully and configured to listen on TCP port **2222**.

Verification steps included:

- Confirming the service started successfully
- Checking the listening port
- Identifying the virtual machine IP address
- Connecting from the host machine using SSH

---

## Attack Simulation

To validate the deployment, an SSH connection was initiated from the host machine to the Kali virtual machine.

The following activities were successfully recorded:

- Incoming SSH connection
- Username used during login
- Authentication success
- Interactive shell session
- Commands executed
- Session termination

These events were stored in Cowrie's log files for later analysis.

---

## Log Analysis

The generated logs contain valuable security information including:

- Timestamp of each event
- Source IP address
- SSH client version
- Login attempts
- Commands entered
- Session duration

This demonstrates how defenders can monitor attacker behavior without exposing production systems.

---

## Skills Demonstrated

- Linux Administration
- SSH Services
- Honeypot Deployment
- Threat Detection
- Log Analysis
- Virtualization
- Cybersecurity Monitoring
- Git Version Control

---

## Screenshots

### 1. Cowrie Installation

Shows the installation and dependency setup.

![Cowrie Installation](screenshots/installation%20process.png)

---

### 2. Honeypot Starting

Shows Cowrie successfully starting.

![Honeypot Starting](screenshots/honeypot%20starting.png)

---

### 3. Listening Service

Verification that Cowrie is listening on port 2222.

![Listening Port](screenshots/hostname.png)

---

### 4. Honeypot Running

Successful SSH connection from the host machine.

![Honeypot Running](screenshots/honeypot_running.png)

---

### 5. Captured Logs

Sample of recorded authentication events and session logs.

![Cowrie Logs](screenshots/Logs.png)

---

## Lessons Learned

Through this project I learned:

- How SSH honeypots simulate real systems
- How attackers interact with exposed SSH services
- How authentication events are recorded
- The importance of log analysis during incident investigations
- How virtualization can be used to safely perform security experiments

---

## Future Improvements

- Integrate Cowrie with Wazuh
- Build an ELK Stack dashboard
- Forward logs to Splunk
- Add GeoIP enrichment for attacker locations
- Create visual analytics dashboards using Python