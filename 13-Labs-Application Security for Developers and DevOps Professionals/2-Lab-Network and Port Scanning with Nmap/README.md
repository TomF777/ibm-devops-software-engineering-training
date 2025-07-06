Types of Nmap Scans with Examples:

1.	`TCP Connect Scan (Default Scan)`:
•	Basic scan that opens a full TCP connection to each target port.
•	Example: nmap -sT target
2.	`SYN Stealth Scan`:
•	Also known as a half-open scan, it sends SYN packets and analyzes responses.
•	Example: nmap -sS target
3.	`UDP Scan`:
•	Sends UDP packets to target ports to identify open UDP services.
•	Example: nmap -sU target
4.	`ACK Scan`:
•	Sends TCP ACK packets to determine firewall configurations.
•	Example: nmap -sA target
5.	`Version Detection (-sV)`:
•	Identifies service versions running on open ports.
•	Example: nmap -sV target
6.	`OS Detection (-O)`:
•	Attempts to identify the target's operating system.
•	Example: nmap -O target
7.	`Script Scanning (-sC)`:
•	Executes predefined scripts to gather additional information.
•	Example: nmap -sC target
8.	`Ping Scans`:
•	Various ping techniques to check target's availability.
•	Example: nmap -PE target (ICMP Echo Request)
9.	`Traceroute (–traceroute)`:
•	Performs traceroute to determine the path packets take.
•	Example: nmap --traceroute target
10.	`TCP Null Scan`:
•	Sends packets with no TCP flags set to observe responses.
•	Example: nmap -sN target
11.	`TCP FIN Scan`:
•	Sends packets with FIN flag set to observe responses.
•	Example: nmap -sF target
12.	`TCP Xmas Scan`:
•	Sends packets with various TCP flags set to observe responses.
•	Example: nmap -sX target


In the `Target` field, enter `scanme.nmap.org`. This routes to your local system.

Choose `Quick Scan` from the scan options.

Click `Scan` to begin the scan process.

Result of `Nmap Output`:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2025-07-05 18:53 Central European Daylight Time

Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.20s latency).
Not shown: 97 closed tcp ports (reset)
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   open     http
5060/tcp filtered sip
```

Now from the list of scan options choose `Intense scan`.

Once the scan finishes, you will see the detailed output along:
```
Not shown: 995 closed tcp ports (reset)

PORT      STATE    SERVICE    VERSION

22/tcp    open     tcpwrapped

| ssh-hostkey: 

|   1024 ac00a01a82ffcc5599dc672b34976b75 (DSA)

|   2048 203d2d44622ab05a9db5b30514c2a6b2 (RSA)

|   256 9602bb5e57541c4e452f564c4a24b257 (ECDSA)

|_  256 33fa910fe0e17b1f6d05a2b0f1544156 (ED25519)

80/tcp    open     tcpwrapped

|_http-favicon: Nmap Project

|_http-title: Go ahead and ScanMe!

| http-methods: 

|_  Supported Methods: GET HEAD POST OPTIONS

|_http-server-header: Apache/2.4.7 (Ubuntu)

5060/tcp  filtered sip

9929/tcp  open     nping-echo Nping echo

31337/tcp open     tcpwrapped

Device type: general purpose

Running: Linux 5.X

OS CPE: cpe:/o:linux:linux_kernel:5

OS details: Linux 5.0 - 5.4

Uptime guess: 46.697 days (since Tue May 20 02:13:08 2025)

Network Distance: 19 hops

TCP Sequence Prediction: Difficulty=261 (Good luck!)

IP ID Sequence Generation: All zeros
```

Click the `Ports/Hosts` tab to see state the ports in the target system. The green indicates open ports and red indicates closed ports.

Click the `Topology` tab to view the visualization of the hosts on this network.  If a host has less than 3 ports, it will be green. If it has 3 to 5 ports it will be yellow. If it has more 6, it will be red. This will be evident when you test on real networks.

Click the Host Details tab to get the details about the host you are scanning. The details will include the Host status, Address, Hostname, Operating system, and so on.


Change the target to `cloud.ibm.com` and click Scan.

