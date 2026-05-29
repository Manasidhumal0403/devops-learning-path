# devops-learning-path
This repository documents my DevOps learning journey, covering Linux fundamentals, shell scripting, Git &amp; GitHub, CI/CD pipelines, Docker, Kubernetes basics, cloud concepts, and monitoring. It includes hands-on practice, scripts, notes, and real-world troubleshooting scenarios as I build practical DevOps skills step by step.


import subprocess
###What is subprocess?subprocess is a Python tool

It allows Python to run Linux commands

👉 Without subprocess, Python cannot talk to Linux commands

# Run Linux command
result = subprocess.run(["df", "-h"], capture_output=True, text=True)

# Get output as lines
lines = result.stdout.split("\n")

# Loop through each line
for line in lines:
    if "/dev/" in line:
        parts = line.split()
        filesystem = parts[0]
        usage = parts[4]  # e.g. 80%

        usage_percent = int(usage.replace("%", ""))

        if usage_percent > 90:
            print("CRITICAL:", filesystem, "usage is", usage)
        elif usage_percent > 75:
            print("WARNING:", filesystem, "usage is", usage)
        else:
            print("OK:", filesystem, "usage is", usage)
