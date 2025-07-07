```
cd CC201/labs/1_ContainersAndDocker/
```

List docker images:
```
docker images
```
### Pull an image from Docker Hub and run it as a container

Pull your first image from Docker Hub:
```
docker pull hello-world
```

Run the hello-world image as a container:
```
docker run hello-world
```

List the containers to see that your container ran and exited successfully:
```
docker ps -a
```

Remove your container:
```
docker container rm <container_id>
```

Verify that that the container has been removed:
```
docker ps -a
```

### Build an image using Dockerfile
See `Dockerfile`

Run the command to build the image:
```
docker build . -t myimage:v1
```

List images to see your image tagged `myimage:v1` in the table:
```
docker images
```

### Run the image as a container

```
docker run -dp 8080:8080 myimage:v1
```

Run the curl command to ping the application as given below
```
curl localhost:8080
```

Stop all running containers:
```
docker stop $(docker ps -q)
```

### Push the image to IBM Cloud Container Registry

Export your namespace as an environment variable 
```
export MY_NAMESPACE=sn-labs-$USERNAME
```

Tag your image so that it can be pushed to IBM Cloud Container Registry:
```
docker tag myimage:v1 us.icr.io/$MY_NAMESPACE/hello-world:1
```

Push the newly tagged image to IBM Cloud Container Registry:
```
docker push us.icr.io/$MY_NAMESPACE/hello-world:1
```

Verify that the image was successfully pushed by listing images in Container Registry:
```
ibmcloud cr images
```

Optionally, to only view images within a specific namespace:
```
ibmcloud cr images --restrict $MY_NAMESPACE
```