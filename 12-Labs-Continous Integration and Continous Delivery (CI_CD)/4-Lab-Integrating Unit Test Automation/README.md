```
cd wtecc-CICD_PracticeCode/labs/04_unit_test_automation/
```

This lab requires installation of the tasks introduced in previous labs. To be sure, apply the previous tasks to your cluster before proceeding.

Reissuing these commands will not hurt anything:
```
kubectl apply -f tasks.yaml
tkn hub install task git-clone
```

Check that you have all of the previous tasks installed:
```
tkn task ls
```

Establish the Workspace:
You also need a PersistentVolumeClaim (PVC) to use as a workspace. Apply the following `pvc.yaml` file to establish the PVC:
```
kubectl apply -f pvc.yaml
```

## Check for cleanup
Check as part of Step 0 for the new `cleanup` task which has been added to `tasks.yaml` file.

Check the pipeline.yaml file which is updated with init that uses the cleanup task.


## Add the flake8 Task
Use the following Tekton CLI command to install the flake8 task into your namespace.
```
tkn hub install task flake8
```

## Modify the Pipeline to Use flake8
Now you will modify the `pipeline.yaml` file to use the new `flake8` task.
```
    - name: lint
      workspaces:
        - name: source
          workspace: pipeline-workspace
      taskRef:
        name: flake8
```

## Modify the Parameters for flake8
Edit `pipeline.yaml`
```
    - name: lint
      workspaces:
        - name: source
          workspace: pipeline-workspace
      taskRef:
        name: flake8
      params:
      - name: image
        value: "python:3.9-slim"
      - name: args
        value: ["--count","--max-complexity=10","--max-line-length=127","--statistics"]
      runAfter:
        - clone
```

Apply these changes to your cluster:
```
kubectl apply -f pipeline.yaml
```

## Run the Pipeline
```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git" \
    -p branch="main" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

## Create a Test Task
Your pipeline also has a placeholder for a `tests` task that uses the `echo` task. Now you will replace it with real unit tests. In this step, you will replace the `echo` task with a call to a unit test framework called `nosetests`.

Edit the `tasks.yaml`:
```
---
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: nose
spec:
  workspaces:
    - name: source
  params:
    - name: args
      description: Arguments to pass to nose
      type: string
      default: "-v"
  steps:
    - name: nosetests
      image: python:3.9-slim
      workingDir: $(workspaces.source.path)
      script: |
        #!/bin/bash
        set -e
        python -m pip install --upgrade pip wheel
        pip install -r requirements.txt
        nosetests $(params.args)
```

Apply these changes to your cluster:
```
kubectl apply -f tasks.yaml
```

## Modify the Pipeline to Use nose
The final step is to use the new `nose` task in your existing pipeline in place of the `echo` task placeholder.
Edit the `pipeline.yaml` file.

```
    - name: tests
      workspaces:
        - name: source
          workspace: pipeline-workspace
      taskRef:
        name: nose
      params:
      - name: args
        value: "-v --with-spec --spec-color"
      runAfter:
        - lint
```

Apply these changes to your cluster:
```
kubectl apply -f pipeline.yaml
```

## Run the Pipeline Again
```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git" \
    -p branch="main" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

You can see the pipeline run status by listing the PipelineRun with:
```
tkn pipelinerun ls
```