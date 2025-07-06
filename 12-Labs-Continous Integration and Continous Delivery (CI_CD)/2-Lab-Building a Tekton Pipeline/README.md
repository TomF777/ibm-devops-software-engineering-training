```
cd wtecc-CICD_PracticeCode/labs/01_base_pipeline/
```

## Create an echo Task
In tasks.yaml:
```
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: hello-task
spec:
  steps:
    - name: echo
      image: alpine:3
      command: [bin/echo]
      args: ["Hello Task!"]
```
Apply it to the cluster:
```
kubectl apply -f tasks.yaml
```

## Create a hello-pipeline Pipeline
will create a very simple pipeline that only calls the `hello-task` task that you just created.

In pipeline.yaml:
```
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: hello-pipeline
spec:
  tasks:
    - name: hello
      taskRef:
        name: hello-task
```

Apply it to the cluster:
```
kubectl apply -f pipeline.yaml
```

## Run the hello-pipeline

Run the pipeline using the Tekton CLI:
```
tkn pipeline start --showlog hello-pipeline
```

## Add a parameter to the task
Make that task a little more useful by making it print any message that you want, not just “Hello Task”.

To do this, you will add a parameter called `message` to the task and use that parameter as the message that it echoes. You will also rename the task to `echo`.
Edit the `tasks.yaml` file to add the parameter to both the input and the echo command:
```
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: echo
spec:
  params:
    - name: message
      description: The message to echo
      type: string
  steps:
    - name: echo-message
      image: alpine:3
      command: [/bin/echo]
      args: ["$(params.message)"]
```
Apply the new task definition to the cluster:
```
kubectl apply -f tasks.yaml
```
## Update the hello-pipeline
You now need to update the pipeline to pass the message that you want to send to the `echo` task so that it can echo the message to the console.
Edit the `pipeline.yaml` file to add the parameter:
```
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: hello-pipeline
spec:
  params:
    - name: message
  tasks:
    - name: hello
      taskRef:
        name: echo
      params:
        - name: message
          value: "$(params.message)"
```

Apply it to the cluster:
```
kubectl apply -f pipeline.yaml
```

## Run the message-pipeline
```
tkn pipeline start hello-pipeline --showlog  -p message="Hello Tekton!"
```

## Create a checkout Task
Create a task that checks out your code from GitHub as the first step in a CD pipeline.
It will create a Tekton task that accepts a repository URL and a branch name and calls git clone to clone your source code.

Edit the `tasks.yaml`:
```
---
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: checkout
spec:
  params:
    - name: repo-url
      description: The URL of the git repo to clone
      type: string
    - name: branch
      description: The branch to clone
      type: string
  steps:
    - name: checkout
      image: bitnami/git:latest
      command: [git]
      args: ["clone", "--branch", "$(params.branch)", "$(params.repo-url)"]
```

Apply it to the cluster:
```
kubectl apply -f tasks.yaml
```

## Create the cd-pipeline Pipeline
Finally, you will create a pipeline called `cd-pipeline` to be the starting point of your Continuous Delivery pipeline.
Edit `pipeline.yaml` file to create a new pipeline called `cd-pipeline`:
```
---
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: cd-pipeline
spec:
  params:
    - name: repo-url
    - name: branch
      default: "master"
  tasks:
    - name: clone
      taskRef:
        name: checkout
      params:
      - name: repo-url
        value: "$(params.repo-url)"
      - name: branch
        value: "$(params.branch)"
```

Apply it to the cluster:
```
kubectl apply -f pipeline.yaml
```

## Run the cd-pipeline
```
tkn pipeline start cd-pipeline \
    --showlog \
    -p repo-url="https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git" \
    -p branch="main"
```

## Fill Out cd-pipeline with Placeholders
Fill out the rest of the pipeline with calls to the `echo` task to simply display a message for now. You will replace these “placeholder” tasks with real ones in future labs.
Update the pipeline.yaml file to include four placeholder tasks.
Edit `pipeline.yaml`:
```
---
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: cd-pipeline
spec:
  params:
    - name: repo-url
    - name: branch
      default: "master"
  tasks:
    - name: clone
      taskRef:
        name: checkout
      params:
      - name: repo-url
        value: "$(params.repo-url)"
      - name: branch
        value: "$(params.branch)"

    - name: lint
      taskRef:
        name: echo
      params:
      - name: message
        value: "Calling Flake8 linter..."
      runAfter:
        - clone

    - name: tests
      taskRef:
        name: echo
      params:
      - name: message
        value: "Running unit tests with PyUnit..."
      runAfter:
        - lint

    - name: build
      taskRef:
        name: echo
      params:
      - name: message
        value: "Building image for $(params.repo-url) ..."
      runAfter:
        - tests

    - name: deploy
      taskRef:
        name: echo
      params:
      - name: message
        value: "Deploying $(params.branch) branch of $(params.repo-url) ..."
      runAfter:
        - build
```

Apply it to the cluster:
```
kubectl apply -f pipeline.yaml
```

## Run the cd-pipeline
```
tkn pipeline start cd-pipeline \
    --showlog \
    -p repo-url="https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git" \
    -p branch="main"
```