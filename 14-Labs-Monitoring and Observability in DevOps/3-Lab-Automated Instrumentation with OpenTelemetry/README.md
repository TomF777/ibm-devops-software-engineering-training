**OpenTelemetry** is an observability framework, an Application programming interface (API), Software Development Kit (SDK), and tools openTelementry aids in generating and collecting application telemetry data such as metrics, logs, and traces.

This lab is an example of how to instrument any application code with `OpenTelemetry` automatically.

## Create a Python Virtual Environment
```
python3 -m venv telemetryenv
```

Activate the virtual environment:
```
source telemetryenv/bin/activate 
```

## Instrumenting the App Automatically Using OpenTelemetry Libraries

Install the opentelemetry-instrumentation-flask and flask packages:
```
pip install opentelemetry-instrumentation-flask flask
```

Ensure the `opentelemetry-distro` Python package is installed.
```
pip install opentelemetry-distro \
    opentelemetry-exporter-otlp \
    opentelemetry-bootstrap -a install
```


Create app.py:
```
from opentelemetry import trace
from flask import Flask, request
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from random import randint
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

app = Flask(__name__) 

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

@app.route("/roll")
def roll():
  with tracer.start_as_current_span(
    "server_request",
    attributes={ "endpoint": "/roll" }
  ):
    sides = int(request.args.get('sides'))
    rolls = int(request.args.get('rolls'))
    return roll_sum(sides,rolls)

def roll_sum(sides, rolls):
  span = trace.get_current_span()
  sum = 0
  for r in range(0,rolls):
    result = randint(1,sides)
    span.add_event( "log", {
      "roll.sides": sides,
      "roll.result": result,
    })
    sum += result
  return  str(sum)
```
Three concepts are seen here: `provider`, `processor`, and `tracer`.
- `provider`: The API entry point that holds configuration. In this case, it is a TracingProvider.

- `processor`: The method of sending the created elements or spans onward.
- `tracer`: An actual object that creates the spans.

The code creates a provider, adds a processor, then configures the local tracing environment to use them.

Run the `opentelemetry-instrument` command with the appropriate parameters to enable auto-instrumentation.

```
opentelemetry-instrument --traces_exporter console flask run
```
The `--traces_exporter` flag specifies the exporter where the traces will go. In this case, you are using the console exporter, which outputs the traces to the console. By modifying the command accordingly, you can replace it with your desired exporter, such as Jaeger or another OpenTelemetry processor.


Send requests to Flask application endpoints using curl or web browser tools:

```
http://127.0.0.1:5000/roll?sides=3&rolls=7
```
```
curl -X GET "http://localhost:5000/roll?sides=6&rolls=3"
```
<br>

View the output.
The output will include a trace ID, span ID, timestamps, span kind, parent ID, status, attributes, events, links, and resource information.
<br>

The attributes will provide information about the HTTP request, such as the HTTP method, server name, scheme, host, target, user agent, peer IP and port, request route, and status code.
```
127.0.0.1 - - [08/Jul/2025 19:48:39] "GET /roll?sides=6&rolls=3 HTTP/1.1" 200 -
{
    "name": "server_request",
    "context": {
        "trace_id": "0xeda37685a8494e0b7a01e04b7b21abd1",
        "span_id": "0xcd5cc788700874ad",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xebbe3fb4b2ecc30f",
    "start_time": "2025-07-08T17:48:39.305362Z",
    "end_time": "2025-07-08T17:48:39.305481Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "endpoint": "/roll"
    },
    "events": [
        {
            "name": "log",
            "timestamp": "2025-07-08T17:48:39.305448Z",
            "attributes": {
                "roll.sides": 6,
                "roll.result": 2
            }
        },
        {
            "name": "log",
            "timestamp": "2025-07-08T17:48:39.305465Z",
            "attributes": {
                "roll.sides": 6,
                "roll.result": 1
            }
        },
```