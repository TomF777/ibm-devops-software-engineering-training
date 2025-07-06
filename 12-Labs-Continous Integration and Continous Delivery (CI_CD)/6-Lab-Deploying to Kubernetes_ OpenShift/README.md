```
cd wtecc-CICD_PracticeCode/labs/06_deploy_to_kubernetes/
```

Install everything from the previous labs:
```
cd /home/project/wtecc-CICD_PracticeCode/labs/06_deploy_to_kubernetes/
tkn hub install task git-clone
```

Check that you have all of the previous tasks installed:
```
tkn task ls
```

## Check for the openshift-client ClusterTask
```
tkn clustertask ls
```

## Reference the openshift-client task
First you need to update the `pipeline.yaml` file to use the new `openshift-client` task.
Open `pipeline.yaml` in the editor and scroll down to the `deploy` pipeline task.

```
    taskRef:
    name: openshift-client
    kind: ClusterTask
```

## Update the Task Parameters
Change the `message` parameter to `SCRIPT` and specify the value of `"oc create deploy $(params.app-name) --image=$(params.build-image)"` in quotes.

Edit `pipeline.yaml`:
```
    - name: deploy
      taskRef:
        name: openshift-client
        kind: ClusterTask
      params:
      - name: SCRIPT
        value: "oc create deploy $(params.app-name) --image=$(params.build-image)"
      runAfter:
        - build
```

## Update the Pipeline Parameters
Add a parameter named `app-name` to the existing list of parameters at the top of the pipeline under `spec.params`.

```
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:  
  name: cd-pipeline
spec:
  workspaces:
    - name: pipeline-workspace
  params:
    - name: app-name
    - name: build-image
    - name: repo-url
    - name: branch
      default: master
```

## Apply Changes and Run the Pipeline
```
kubectl apply -f pipeline.yaml
```

Start the Pipeline
```
tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git" \
    -p branch=main \
    -p app-name=hitcounter \
    -p build-image=image-registry.openshift-image-registry.svc:5000/$SN_ICR_NAMESPACE/tekton-lab:latest \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    --showlog
```

Check the Run Status:
```
tkn pipelinerun ls
```

You can check the logs of the last run with:
```
tkn pipelinerun logs --last
```

## Check the Deployment
Now, check to see if the deployment is running. Use the `kubectl` command to check that your deployment is in a running state.

```
kubectl get all -l app=hitcounter
```