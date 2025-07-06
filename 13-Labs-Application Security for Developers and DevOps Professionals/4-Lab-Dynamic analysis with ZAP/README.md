In this lab, you will learn how to install, configure, and use OWASP ZAP for dynamic analysis of your project code.

### What is Dynamic Code Analysis?
It is the testing and evaluation of an application during runtime. Also referred to as dynamic code scanning, dynamic analysis can identify security issues that are too complicated for static analysis alone to reveal.

Dynamic application security testing (DAST) looks at the application from the outside-in — by simulating attacks against a web application and analyzing the application’s responses to discover security vulnerabilities in the application.

In this lab, you get hands-on experience using OWASP ZAP to conduct dynamic analysis. A real-world application that you will be testing is the OWASP Juice Shop app, which is an application developed for security training purposes. 

## Fetch the Insecure App: Juice Shop
```
docker pull bkimminich/juice-shop
docker run --rm -p 3000:3000 bkimminich/juice-shop
```

## Launch the Juice Shop UI
```
http://localhost:3000
```

## Run ZAP (Zed Attack Proxy)
```
docker pull zaproxy/zap-stable
```

Run the basic scan:
```
docker run -v $(pwd):/zap/wrk/:rw -t zaproxy/zap-stable zap-baseline.py -t <target_url> -g gen.conf -r zap-report.html
```

Run the full scan:
```
docker run -v $(pwd):/zap/wrk/:rw -t zaproxy/zap-stable zap-full-scan.py -t <target_url> -g gen.conf -r zap-report.html
```

Replace `<target_url>` with the URL of the web application you want to scan.

It could also be docker container name of the web app.

## Interpret the scan results
A number of items tested came back with `PASS:` so we will not look at those.
Our attention is on any warnings or failures. 

You can use the numbers next to the vulnerability names to read about the alert on the ZAP Proxy Web site. Using the following URL:
```
https://www.zaproxy.org/docs/alerts/{NUMBER}
```