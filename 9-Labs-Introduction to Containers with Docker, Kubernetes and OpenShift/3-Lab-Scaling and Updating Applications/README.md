```
cd CC201/labs/3_K8sScaleAndUpdate/
```

### Build application 

```
export MY_NAMESPACE=sn-labs-$USERNAME
docker build -t us.icr.io/$MY_NAMESPACE/hello-world:1 . && docker push us.icr.io/$MY_NAMESPACE/hello-world:1
```

### Deploy the application to Kubernetes
```
sudo kubectl apply -f deployment.yaml
```

List Pods until the status is “Running”:
```
sudo kubectl get pods
```

In order to access the application, we have to expose it to the internet via a Kubernetes Service:
```
sudo kubectl expose deployment/hello-world
```

Run this command in the new terminal window:
```
sudo kubectl proxy
```

Go back to your original terminal window, ping the application to get a response:
```
curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy
```

Observe the message “Hello world from hello-world-xxxxxxxx-xxxx. Your app is up and running!


### Scaling the application using a ReplicaSet

Use the `scale` command to scale up your Deployment.
```
sudo kubectl scale deployment hello-world --replicas=3
```

Get Pods to ensure that there are now three Pods instead of just one:
```
kubectl get pods
```

Ping the application multiple times to ensure that Kubernetes is load-balancing across the replicas:
```
for i in `seq 10`; do curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy; done
```

You should see that the queries are going to different Pods because of the effect of load-balancing.

Similarly, you can use the scale command to scale down your Deployment:
```
sudo kubectl scale deployment hello-world --replicas=1
```

Check the Pods to see that two are deleted or being deleted.
```
sudo kubectl get pods
```

### Perform rolling updates

Edit `app.js`.

Change the welcome message from `'Hello world from ' + hostname + '! Your app is up and running!\n'` to `'Welcome to ' + hostname + '! Your app is up and running!\n'`

Build and push this new version to Container Registry (update the tag to version 2)
```
docker build -t us.icr.io/$MY_NAMESPACE/hello-world:2 . && docker push us.icr.io/$MY_NAMESPACE/hello-world:2
```

Update the deployment to use this version instead:
```
sudo kubectl set image deployment/hello-world hello-world=us.icr.io/$MY_NAMESPACE/hello-world:2
```

Get a status of the rolling update by using the following command:
```
sudo kubectl rollout status deployment/hello-world
```

You can also get the Deployment with the wide option to see that the new tag is used for the image:
```
sudo kubectl get deployments -o wide
```
Look for the `IMAGES` column and ensure that the tag is `2`.

Ping the application to ensure that the new welcome message is displayed.
```
curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy
```

It’s possible that a new version of an application contains a bug. In that case, Kubernetes can roll back the Deployment like this:
```
sudo kubectl rollout undo deployment/hello-world
```

Get a status of the rolling update by using the following command:
```
sudo kubectl rollout status deployment/hello-world
```

Get the Deployment with the `wide` option to see that the old tag is used.
```
sudo kubectl get deployments -o wide
```

Look for the `IMAGES` column and ensure that the tag is `1`.

Ping your application to ensure that the earlier ‘Hello World..Your app is up & running!‘ message is displayed.
```
curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy
```

### Using a ConfigMap to store configuration
ConfigMaps and Secrets are used to store configuration information separate from the code so that nothing is hardcoded.

Create a ConfigMap that contains a new message:
```
sudo kubectl create configmap app-config --from-literal=MESSAGE="This message came from a ConfigMap!"
```

Use the Explorer to edit `deployment-configmap-env-var.yaml.` Insert namespace where it says `<my_namespace>`.

Use the Explorer to open the `app.js` file.

Replace 
`res.send('Welcome to ' + hostname + '! Your app is up and running!\n')`

with

`res.send(process.env.MESSAGE + '\n')`

Build and push a new image that contains your new application code:
```
sudo docker build -t us.icr.io/$MY_NAMESPACE/hello-world:3 . && docker push us.icr.io/$MY_NAMESPACE/hello-world:3
```

Apply the new Deployment configuration:
```
sudo kubectl apply -f deployment-configmap-env-var.yaml
```

Ping your application again to see if the message from the environment variable is returned:
```
curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy
```

Using the following command, delete the old ConfigMap and create a new one with the same name but a different message:
```
sudo kubectl delete configmap app-config && kubectl create configmap app-config --from-literal=MESSAGE="This message is different, and you didn't have to rebuild the image!"
```

Restart the Deployment so that the containers restart. This is necessary since the environment variables are set at start time:
```
sudo kubectl rollout restart deployment hello-world
```

Ping your application again to see if the new message from the environment variable is returned:
```
curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy
```

### Autoscale the hello-world application using Horizontal Pod Autoscaler

Add the following section to the `deployment.yaml` file under the `template.spec.containers` section for increasing the CPU resource utilization:
```
        name: http
    resources:
        limits:
            cpu: 50m
        requests:
            cpu: 20m
```

Apply the deployment:
```
sudo kubectl apply -f deployment.yaml
```

Autoscale the `hello-world` deployment:
```
sudo kubectl autoscale deployment hello-world --cpu-percent=5 --min=1 --max=10
```

Check the current status of the newly-made HorizontalPodAutoscaler:
```
sudo kubectl get hpa hello-world
```

Ensure that the kubernetes proxy is still running in the 2nd terminal. If it is not, please start it again by running:
```
sudo kubectl proxy
```

Open another new terminal and enter the below command to spam the app with multiple requests for increasing the load:
```
for i in `seq 100000`; do curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy; done
```

Run the below command in separate terminal to observe the replicas increase in accordance with the autoscaling:
```
sudo kubectl get hpa hello-world --watch
```

You will see an increase in the number of replicas which shows that your application has been autoscaled.

Stop this command by pressing `CTRL + C`.

Run the below command to observe the details of the horizontal pod autoscaler:
```
sudo kubectl get hpa hello-world
```

Delete the Deployment:
```
sudo kubectl delete deployment hello-world
```

Delete the Service:
```
sudo kubectl delete service hello-world
```