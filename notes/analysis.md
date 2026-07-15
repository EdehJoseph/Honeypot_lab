# Cowrie Honeypot Findings

## Objective

Deploy a Cowrie SSH honeypot on Kali Linux and observe SSH login attempts.

## Environment

- Host OS: macOS
- Virtualization: VMware Fusion
- Guest OS: Kali Linux
- Honeypot: Cowrie

## Findings

- Successfully deployed a Cowrie SSH honeypot.
- Generated SSH login attempts from a macOS host.
- Captured authentication attempts in Cowrie logs.
- Parsed log data using Python.
- Visualized attacker activity using Matplotlib.

## Skills Demonstrated

- Honeypot Deployment
- Linux Administration
- Log Analysis
- Python Scripting
- Threat Detection
- Security Monitoring

## Future Improvements

- Forward Cowrie logs to Wazuh.
- Integrate with ELK Stack or Splunk.
- Add GeoIP enrichment for source IPs.
- Automate alert generation.