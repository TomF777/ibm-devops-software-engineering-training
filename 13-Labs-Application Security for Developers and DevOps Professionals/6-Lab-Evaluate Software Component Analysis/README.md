Software Composition Analysis (SCA) is the process of identifying areas of risk that result from the use of third-party and open-source components during application development.

`Dependency-Check` is a Software Composition Analysis (SCA) tool that attempts to detect publicly disclosed vulnerabilities contained within a project’s dependencies. Dependencies are the software components that your code relies on for additional functionality. The SCA tool will generate a report listing the dependency, any identified Common Platform Enumeration (CPE) identifiers, and the associated Common Vulnerability and Exposure (CVE) entries.

In this hands-on lab, we will explore the use of the `OWASP SCA Dependency-checker` tool.


## Install the OWASP SCA Tool
Install Java if not installed already:
```
sudo apt install default-jdk
```

Install the OWASP SCA Tool
```
wget -O dependency-check.zip https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0267EN-SkillsNetwork/labs/module2/data/dependency-check.zip && unzip dependency-check.zip && chmod +x dependency-check/bin/dependency-check.sh && sudo echo "alias dependency-check=$(pwd)/dependency-check/bin/dependency-check.sh" >> ~/.bashrc && source ~/.bashrc
```
or just install from existing folder
```
chmod +x dependency-check/bin/dependency-check.sh && sudo echo "alias dependency-check=$(pwd)/dependency-check/bin/dependency-check.sh" >> ~/.bashrc && source ~/.bashrc
```

## Download the Source Code
```
git clone https://github.com/juice-shop/juice-shop.git
```

The `juice-shop app` is laready in this lab folder

## Run SCA on Juice Shop Components
Use the dependency-check command on the Juice Shop source code:
```
dependency-check -f JSON --prettyPrint --scan juice-shop
```

The command will produce a file called `dependency-check-report.json` which may contain information about any vulnerable components found by the OWASP SCA Tool.

## Analyzing JSON Results

In a secure Software Development Life Cycle (SDLC), each component should be thoroughly checked and verified for security. Any dependencies that might be vulnerable should be upgraded or replaced.

## Creating an HTML report
Reports outputted to JSON format can be difficult to read. It may be preferable to send your scan output to an HTML report instead. HTML reports are easier for us to read and interpret.

Use the `dependency-check` command to create an HTML report from a `--scan` of the `juice-shop` folder:
```
dependency-check --scan juice-shop
```