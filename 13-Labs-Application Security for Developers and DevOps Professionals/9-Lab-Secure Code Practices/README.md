In this lab, you will look at how you can make your code more secure and then practice what you have learned. You will practice how to write more secure code in Python web applications written with the Flask framework.

Security Code Practices are a set of practices that developers follow to ensure their application is secure from the beginning of the software development lifecycle. Some practices we will follow are:

- Setting HTTP headers
- Implementing Cross Origin Resource Sourcing (CORS) policies
- Working with Credentials and GitHub
- Using the Vault


## Improving security with HTTP headers
The first thing you can do to improve the security of your application is set secure HTTP headers. You can do this by simply wrapping your flask application with a Python package called `Flask-Talisman`.

This code doesn't implement security:
```
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Base URL for our service"""
    return return "Hello Flask"

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)
```
### Security Improvement
This version of the application uses `Flask-Talisman` to add security headers that reject loading content from other sites, making your application more secure.

```
pip install flask-talisman
```

```
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
# Create a content security policy and apply it
SELF = "'self'"
csp = {
    'default-src': SELF
}

talisman = Talisman(app, force_https=False, content_security_policy=csp)

@app.route("/")
def hello():
    return "Hello Flask"


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)
```

Run the flask app:
```
flask run
```
or 
```
flask run --host=0.0.0.0 --port=5000
```
to be accessible outside of the host.

The security policy:
```
csp = {
    'default-src': SELF
}
```
is the default policy. A Web site administrator wants all content to come from the site’s own origin (this excludes subdomains.) This means that you cannot have things like libraries, images, and fonts on your Web site that are loaded from other sites. If you need this, you must specify it in the content security policy.



