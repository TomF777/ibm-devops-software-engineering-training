```
cd jmgdo-microservices/swagger_example
```

```
python3 -m pip install flask_cors
```

start the application which serves the REST API on port number 5000.
```
python3 app.py
```

Copy the URL of the application

Edit `swagger_config.json` and enter the URL into `<Your application URL>`.

Copy the entire content of the file swagger_config.json. You will need this copied content to generate SwaggerUI.

Open the link `https://editor.swagger.io/` to go to the Swagger Editor.

From the File menu, click on Clear Editor to clear the content of the Swagger Editor.

Paste the content you copied from `swagger_config.json` on the left side. You will get a prompt which says `Would you like to convert your JSON into YAML?`. Press `Cancel` to paste the content.

You will see that the UI is automatically populated on the right.

Now you can test each of the endpoints.


### Creating Swagger Documentation and Generating Server code

Copy and paste following JSON in the Swagger Editor.
You will get a prompt which says `Would you like to convert your JSON into YAML?`. Press Cancel to paste the content.
```
{
    "swagger": "2.0",
    "info": {
      "version": "1.0",
      "title": "Our first generated REST API",
      "description": "<h2>This is a sample server code the is generated from Swagger Documenation with Swagger Editor</h2>"
    },

    "paths": {
      "/greetings": {
        "get": {
          "summary": "Returns a list of Greetings",
          "tags": ["Hello in Different Languages"],
          "description": "Returns greetings in different languages",
          "produces": [
            "application/json"
          ],
          "responses": {
            "200": {
              "description": "OK"
            }
          }
        }
      }
    }
}
```

You will see the Swagger UI automatically appearing on the right. You cannot test it yet as your application is not defined and running yet.

From the menu on top, click on `Generate Server` and select python-flask. This will automatically generate the server code as a zip file named `python-flask-server-generated.zip.` Download the zip file to your system.

Unzip the downloaded folder.

```
cd python-flask-server-generated/python-flask-server
```

The entire server setup along with endpoint is done for you already. Let's build the server code.
```
docker build . -t mynewserver
```

Run the docker application now by running the following command. The server generated code automatically is configured to run on port 8080.
```
docker run -dp 8080:8080 mynewserver
```

To confirm that the service is running and your REST API works, execute the following command:
```
curl localhost:8080/greetings
```

Next, in the file explorer go to, `python-flask-server-generated/python-flask-server/swagger_server/controllers/hello_in_different_languages_controller.py`.
This is where you need to implement your actual response for the REST API.

Insert the code:
```
hellos = {
  "English": "hello",
  "Hindi": "namastey",
  "Spanish": "hola",
  "French": "bonjour",
  "German": "guten tag",
  "Italian": "salve",
  "Chinese": "nǐn hǎo",
  "Portuguese": "olá",
  "Arabic": "asalaam alaikum",
  "Japanese": "konnichiwa",
  "Korean": "anyoung haseyo",
  "Russian": "Zdravstvuyte"
}

return hellos
```

Rebuild the docker image and run again the container:
```
docker build . -t mynewserver
docker run -p 8080:8080 mynewserver
```

Now click on Launch Application and enter the port number 8080. This will open a browser window. Append the path /greetings to the URL. You should see the greetings in the page.