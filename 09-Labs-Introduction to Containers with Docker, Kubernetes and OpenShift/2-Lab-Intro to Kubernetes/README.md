```
cd CC201/labs/2_IntroKubernetes/
```

Verify that kubectl CLI is installed:
```
kubectl version
```

Get cluster information:
```
sudo kubectl config get-clusters
```

A `kubectl` context is a group of access parameters, including a cluster, a user, and a namespace. View your current context with the following command:
```
sudo kubectl config get-contexts
```

List all the Pods in your namespace:
```
sudo kubectl get pods
```

### Create a Pod with an imperative command

Export your namespace as an environment variable so that it can be used in subsequent commands:

```
export MY_NAMESPACE=sn-labs-$USERNAME
```

Build and push the image again:

```
docker build -t us.icr.io/$MY_NAMESPACE/hello-world:1 . && docker us.icr.io/$MY_NAMESPACE/hello-world:1push 
```

Run the hello-world image as a container in Kubernetes:
```
kubectl run hello-world-container --image us.icr.io/$MY_NAMESPACE/hello-world:1 --overrides='{"spec":{"template":{"spec":{"imagePullSecrets":[{"name":"icr"}]}}}}'
```

The `--overrides` option here enables us to specify the needed credentials to pull this image from IBM Cloud Container Registry.

<br>

List the Pods in your namespace:
```
sudo kubectl get pods
```


You can also specify the wide option for the output to get more details about the resource:
```
sudo kubectl get pods -o wide
```

Describe the Pod to get more details about it:

```
sudo kubectl describe pod hello-world-container

```

Delete the Pod:
```
sudo kubectl delete pod hello-world-container
```

### Create a Pod with imperative object configuration
See `hello-world-create.yaml `

Imperatively create a Pod using the provided configuration file:
```
sudo kubectl create -f hello-world-create.yaml
```

List the Pods in your namespace:
```
sudo kubectl get pods
```

Delete the Pod:
```
kubectl delete pod hello-world
```

### Create a Pod with a declarative command
See `hello-world-apply.yaml`

Edit `hello-world-apply.yaml`. You need to insert your namespace where it says `<my_namespace>`.

<br>

Use the kubectl apply command to set this configuration as the desired state in Kubernetes:
```
sudo kubectl apply -f hello-world-apply.yaml
```

Get the Deployments to ensure that a Deployment was created:
```
sudo kubectl get deployments
```

List the Pods to ensure that three replicas exist:
```
sudo kubectl get pods
```

With `declarative` management, if you delete a Pod now, a new one will be created in its place to maintain three replicas.
```
sudo kubectl delete pod <pod_name> && kubectl get pods
```

List the Pods to see a new one being created.
```
sudo kubectl get pods
```
<br>

### Load balancing the application

Let’s expose our application to the internet and see how Kubernetes load balances requests.

In order to access the application, we have to expose it to the internet using a Kubernetes Service.
```
sudo kubectl expose deployment/hello-world
```

List Services in order to see that this service was created:
```
sudo kubectl get services
```

Since the cluster IP is not accessible outside of the cluster, we need to create a proxy.
```
sudo kubectl proxy
```
This command doesn’t terminate until you terminate it. Keep it running so that you can continue to access your app.


In the original terminal window, ping the application to get a response.

```
curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy
```

Run the command which runs a for loop ten times creating 10 different pods and note names for each new pod.

```
for i in `seq 10`; do curl -L localhost:8001/api/v1/namespaces/sn-labs-$USERNAME/services/hello-world/proxy; done
```
You should see more than one Pod name, and quite possibly all three Pod names, in the output. This is because Kubernetes load balances the requests across the three replicas, so each request could hit a different instance of our application.

Delete the Deployment and Service:
```
kubectl delete deployment/hello-world service/hello-world
```

Return to the terminal window running the `proxy` command and kill it using `Ctrl+C`