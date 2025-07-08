This lab uses Docker to run both Prometheus, and special Node Exporters, which will behave like servers that you can monitor. 

```
docker pull bitnami/node-exporter:latest
```

```
docker pull bitnami/prometheus:latest
```

## Start the first node exporter
Start up three node exporters listening on port `9100` and forwarding to ports `9101`, `9102`, and `9103`, respectively.

Create a docker network:
```
docker network create monitor
```
<br>

Start a first node exporter instance on the `monitor` network:

```
docker run -d --name node-exporter1 -p 9101:9100 --network monitor bitnami/node-exporter:latest
```
Check if the instance is running by launching the application on port 9101:
```
http://localhost:9101
```
There should be the Node Exporter page open up with a hyperlink to Metrics.

## Start two more node exporters
Start two more node exporter containers, so that Prometheus has three nodes to monitor in total.
```
docker run -d --name node-exporter2 -p 9102:9100 --network monitor bitnami/node-exporter:latest
```

```
docker run -d --name node-exporter3 -p 9103:9100 --network monitor bitnami/node-exporter:latest
```

Check if all the instances of node exporter are running:
```
docker ps | grep node-exporter
```

## Configure and run Prometheus

Create a configuration file called `prometheus.yml` to instruct Prometheus on which nodes to monitor.

```
touch ./prometheus.yml
```

Edit the file:
```
# my global config
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. The default is every 1 minute.

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['node-exporter1:9100']
        labels:
          group: 'monitoring_node_ex1'
      - targets: ['node-exporter2:9100']
        labels:
          group: 'monitoring_node_ex2'
      - targets: ['node-exporter3:9100']
        labels:
          group: 'monitoring_node_ex3'
```
Notice that while you access the node exporters externally on ports `9101`, `9102`, and `9103`, they are internally all listening on port `9100`, which is how Prometheus will communicate them on the monitor network.

Finally, you can launch the Prometheus monitor:
```
docker run -d --name prometheus -p 9090:9090 --network monitor \
-v $(pwd)/prometheus.yml:/opt/bitnami/prometheus/conf/prometheus.yml \
bitnami/prometheus:latest
```


## Open the Prometheus UI

Launch the Prometheus web UI:

```
http://localhost:9090
```

In the Prometheus application, click `Status` on the menu and choose `Targets` (or `Target health`) to see which targets are being monitored.

View the status of all three node exporters.

## Execute your first query

Navigate to main page of Prometheus (upper left `Prometheus` icon) and click on `Graph`.

Insert:
```
node_cpu_seconds_total
```

It will query the nodes for the total CPU seconds and show graphs of it.

Next, click `Table` to see the CPU seconds for all the targets in tabular format.

Now, filter the query to get the details for only one instance `node-exporter2` using the following query.
```
node_cpu_seconds_total{instance="node-exporter2:9100"}
```

## Stop one node exporter and observe

```
docker stop node-exporter1
```

Go back to the `Prometheus UI` on your browser and check the targets by selecting the menu item `Status` -> `Targets`.

You should now see that one of the node exporters that are being monitored is down.

## Enable Python application for Monitoring

You must instrument your application to emit metrics on an endpoint called `/metrics` in order for Prometheus to be able to monitor your application.
There is a Python package called `Prometheus Flask exporter` for Prometheus that will do this.

Create file named `pythonserver.py`.

Create `Dockerfile`.

Build a Docker image:
```
docker build -t pythonserver .
```

run the pythonserver Docker container on the monitor network exposing port 8080 so that Prometheus can access it:
```
docker run -d --name pythonserver -p 8081:8080 --network monitor pythonserver
```

Check that the Python server is running:
```
http://localhost:8081/
http://localhost:8081/home
http://localhost:8081/contact
```

## Reconfigure Prometheus
Prometheus needs to know about the new `pythonserver` node to monitor.

Edit `prometheus.yml`. Add new job:

```
  - job_name: 'monitorPythonserver'
    static_configs:
      - targets: ['pythonserver:8080']
        labels:
          group: 'monitoring_python'
```

Restart the prometheus server 
```
docker restart prometheus
```

Check the Prometheus UI to see the new Targets.

## Monitor your application
In order to see some results of monitoring, you need to generate some network traffic.

Make multiple requests to the three endpoints of the Python server:
```
curl localhost:8081
curl localhost:8081/home
curl localhost:8081/contact
```

Use the Prometheus UI to query for the following metrics:
```
flask_http_request_duration_seconds_bucket
flask_http_request_total
process_virtual_memory_bytes
```

If you are interested in what other metrics are being emitted by your application, you can view all of the metrics that your application is emitting by opening the `/metrics` endpoint.

