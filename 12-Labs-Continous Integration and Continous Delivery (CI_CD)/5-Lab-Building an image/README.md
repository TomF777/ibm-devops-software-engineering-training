```
cd wtecc-CICD_PracticeCode/labs/05_build_an_image/
```

Issue the following commands to install everything from the previous labs.
```
tkn hub install task git-clone
```

Check that you have all of the previous tasks installed:
```
tkn task ls
```

## Check for ClusterTasks
Your pipeline currently has a placeholder for a `build` step that uses the `echo` task. Now it is time to replace it with a real image builder.
Check that the `buildah` task is installed as a ClusterTask using the Tekton CLI.
```
tkn clustertask ls
```

## Add a Workspace to the Pipeline Task
Update the `pipeline.yaml` file to use the new `buildah` task.
Edit `pipeline.yaml`:
```
    - name: build
      workspaces:
        - name: source
          workspace: pipeline-workspace
      taskRef:
        name: echo
      params:
      - name: message
        value: "Building image for $(params.repo-url) ..."
      runAfter:
        - tests
```

## Reference the buildah Task
You need to reference the new buildah task that you want to use.

Edit `pipeline.yaml`:
```
    - name: build
      workspaces:
        - name: source
          workspace: pipeline-workspace
      taskRef:
        name: buildah
        kind: ClusterTask
      params:
      - name: message
        value: "Building image for $(params.repo-url) ..."
      runAfter:
        - tests
```

## Update the Task Parameters
Edit `pipeline.yaml`.
Change the `message` parameter to `IMAGE` and specify the value of `$(params.build-image)`:

```
    - name: build
      workspaces:
        - name: source
          workspace: pipeline-workspace
      taskRef:
        name: buildah
        kind: ClusterTask
      params:
      - name: IMAGE
        value: "$(params.build-image)"
      runAfter:
        - tests
```


Now that you are passing in the `IMAGE` parameter to this task, you need to go back to the top of the `pipeline.yaml` file and add the parameter there so that it can be passed into the pipeline when it is run.
Add a parameter named `build-image` to the existing list of parameters at the top of the pipeline under `spec.params`.

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
      default: master
    - name: build-image
```

## Apply Changes and Run the Pipeline
```
kubectl apply -f pipeline.yaml
kubectl apply -f pvc.yaml
```

## Start the Pipeline
```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git" \
    -p branch=main \
    -p build-image=image-registry.openshift-image-registry.svc:5000/$SN_ICR_NAMESPACE/tekton-lab:latest \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

Check the Run Status
```
tkn pipelinerun ls
```

You can check the logs of the last run with:
```
tkn pipelinerun logs --last
```