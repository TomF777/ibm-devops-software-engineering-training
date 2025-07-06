```
cd wtecc-CICD_PracticeCode/labs/03_use_tekton_catalog/
```

This lab requires installation of the tasks introduced in previous labs. To be sure, apply the previous tasks to your cluster before proceeding:
```
kubectl apply -f tasks.yaml
```

## Add the git-clone Task

Use this command to install the `git-clone` task from Tekton Hub:
```
tkn hub install task git-clone --version 0.8
```

## Create a Workspace

Apply the new task definition to the cluster:
```
kubectl apply -f pvc.yaml
```

## Add a Workspace to the Pipeline
Edit the `pipeline.yaml` file and add a `workspaces`: 
```
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: cd-pipeline
spec:
  workspaces:
    - name: pipeline-workspace
  params:
    - name: repo-url
    - name: branch
      default: "master"
  tasks:
    - name: clone
      workspaces:
        - name: output
          workspace: pipeline-workspace
      taskRef:
        name: git-clone
      params:
      - name: url
        value: $(params.repo-url)
      - name: revision
        value: $(params.branch)

    # Note: The remaining tasks are unchanged. Do not delete them.
```

Apply the pipeline to your cluster:
```
kubectl apply -f pipeline.yaml
```

## Run the Pipeline
You can now use the Tekton CLI (tkn) to create a PipelineRun to run the pipeline.
```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git" \
    -p branch="main" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

You can check the logs of the last run with:
```
tkn pipelinerun logs --last
```