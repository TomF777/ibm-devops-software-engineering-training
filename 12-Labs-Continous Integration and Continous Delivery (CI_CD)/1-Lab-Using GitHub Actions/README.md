```
cd wtecc-CICD_PracticeCode
```

## Create a Workflow
```
mkdir -p .github/workflows
touch .github/workflows/workflow.yml
```
In workflow.yml:
```
name: CI workflow
```

## Add Event Triggers
In workflow.yml:
```
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
```

## Add a Job
In workflow.yml:
```
jobs:
  build:
    runs-on: ubuntu-latest
```

## Target Python 3.9
In workflow.yml:
```
jobs:
  build:
    runs-on: ubuntu-latest
    container: python:3.9-slim
```

Open the terminal and configure your email and user name:
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

git add -A
git commit -m "COMMIT MESSAGE"
git push
```

## Add the checkout Step
In workflow.yml:
```
jobs:
  build:
    runs-on: ubuntu-latest
    container: python:3.9-slim
    steps:
      - name: Checkout
        uses: actions/checkout@v3
```

## Install Dependencies
In workflow.yml:
```
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
```

## Code quality check with flake8
In workflow.yml:
```
      - name: Lint with flake8
        run: |
          flake8 service --count --select=E9,F63,F7,F82 --show-source --statistics
          flake8 service --count --max-complexity=10 --max-line-length=127 --statistics
```


## Test Code Coverage with nosetests
In workflow.yml:
```
     - name: Run unit tests with nose
        run: nosetests -v --with-spec --spec-color --with-coverage --cover-package=app
```

## Push Code to GitHub
```
git add -A
git commit -m "COMMIT MESSAGE"
git push
```

## Run the Workflow

Open the Actions tab in the forked repository in your GitHub account. Click the CI workflow action. Pushing changes in the previous step should have triggered a build action and it should be visible in the Actions tab.
