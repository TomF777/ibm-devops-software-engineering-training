```
docker network create mynet
```

```
docker run --name postgres  -e POSTGRES_USER=root -e POSTGRES_PASSWORD=Test12345  -p 5432:5432 --network mynet -d postgres
```

```
docker run -d --name sonarqube -p 9000:9000 -e sonar.jdbc.url=jdbc:postgresql://postgres/postgres -e sonar.jdbc.username=root -e sonar.jdbc.password=Test12345 --network mynet sonarqube
```

Check that both containers are running:
```
docker ps
```

## Log in to SonarQube
Launch SonarQube on `http://localhost:9000`

username: admin

password: admin

You will be prompted to change your password.

#### Create a SonarQube Project:
Click on the `Manually` icon on the bottom left.

On the next page, create a project by following these steps:
1.	Set the project display name to `temp`.
2.	Set the project key to `temp` (this will happen by default).
3.	Ensure the `main` branch is selected
4.	Press the `Next` button to continue.

Select `Use the global setting` and then click on `Create project`.

On the next page, where it asks how you want to analyze your repository, select the `Locally` option.

## Generate SonarQube Scanner Token
You can generate a token on the `Analyze your project` page at the `Provide a token` step.
Click the `Generate` button.

Copy the token and then paste it in a safe place.

Then click the `Continue` button.

On next page `Run analysis on your project` select configuration:

`Other (for JS, TS, Go, Python, PHP, ...)`

`Linux`

`Copy` - Copy the scanner command and paste it in a safe place.

## Ready the SonarQube Scanner

SonarQube server that stores the results of scans is separate and distinct from the SonarQube scanner which performs the actual scanning. Up until now, we’ve created a database for storing the analysis results and provisioned a SonarQube server for serving the UI.

To get the SonarQube scanner to work in the Cloud IDE, you can either install it locally or pull its docker image and run its docker container. In this lab, you will be pulling the docker image and running its docker container.

Download the `sonarsource/sonar-scanner-cli` image from Docker hub:
```
docker pull sonarsource/sonar-scanner-cli
```

Run the following bash `alias` command in the terminal, which creates an alias `sonar-scanner` for running the scanner later using the `scanner-cli` docker container in the same docker network as SonarQube server:

```
alias sonar-scanner='docker run --rm --network mynet  -v "$(pwd):/usr/src" sonarsource/sonar-scanner-cli'
```

Any arguments that you pass into the `sonar-scanner` command will be passed into the container version as well. This is how you can easily run commands in Docker containers as if they were actually installed on your computer.

## Getting a Sample Project
You need some code to scan.
```
cd wtecc-CICD_PracticeCode
```

## Running the Scanner
In the terminal, run the command you saved from step `Generate SonarQube Scanner Token`, but for host.url enter the container name of the SonarQube server.
e.g.
```
sonar-scanner \
  -Dsonar.projectKey=temp \
  -Dsonar.sources=.  \
  -Dsonar.host.url=http://sonarqube:9000  
  -Dsonar.token=sqp_2e59e79afd7709f63cd161fdf72fa5ff22ce766b
```

Once you hit enter, the scanner starts a static analysis in your current project directory and will run for a while.


## Interpret the scan results
Once the code scan and analysis are done, you can view the results on the SonarQube UI in `Overall Code` tab.

If you view the report, you will see that the overall report is passing, but there is one security item that is flagged.

If you click the link for the 1 next to Security Hotspots you will see some information about it.
Across the top tabs you can see the following labels:

• Where is the risk?

• What’s the risk?

• Assess the risk

• How can I fix it?

Under the `Where is the risk?` tab, the report is telling you that there is a potential Cross Site Request Forgery `(CSRF)` risk because the sample code we used didn’t include appropriate security measures to protect it.
Your next question might be, “How can I fix it?” 
You can find that out by clicking the `How can I fix it?` tab.

This application is written using the Flask framework. If you scroll down to the section about Flask, it tells you exactly how to use the `CSRFProtect` class to fix the problem, along with some other advice.
```
app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app) # Compliant
```

If this were your original code, you would want to make the suggested changes to your application and run the scan again to be sure that it was fixed.










