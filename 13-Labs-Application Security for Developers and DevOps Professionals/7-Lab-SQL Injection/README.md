SQL injection (SQLi) is a type of vulnerability in which the attacker accesses private information with SQL queries in the user input field that modify execution of SQL commands.

In this lab, we will look at SQL manipulation, which is common in web applications.


In this lab, you will:
- Identify SQL injection in a Python web application
- Use `Bandit` to scan for vulnerabilities in the Python source code
- Resolve SQL injection vulnerabilities by correcting the source code
- Retest code fixes to confirm that the vulnerability was mitigated


## Installing Bandit
`Bandit` is an open-source static application security testing (SAST) tool that can scan for vulnerabilities in web applications written in Python.
```
pip install bandit
```

## Source Code
Use `web_app_example.py`

## Find the Vulnerability
`Bandit` makes it easy to scan Python files inside the terminal window.

```
bandit -r web_app_example.py
```

Bandit's analysis identifies the exact location of the vulnerability:
```
Location: web_app_example.py:16:8
```

Under the "Test results" section, we see that Bandit has identified one issue - "Possible SQL injection vector through string-based query construction". Bandit also provided us with the exact location where the vulnerability occurred: line 16. Now we're aware that the syntax used in the SQL query introduces risk. Let's take a closer look at why the query was identified as a SQL injection vulnerability.

## Mitigate the Vulnerability
Change the SQL query on lines 16 & 17 in the python code:
```
sql = "SELECT * FROM users WHERE username = %s AND password = %s"
cursor.execute(sql, (username, password))
```

## Check for Successful Fix
```
bandit -r web_app_example.py
```