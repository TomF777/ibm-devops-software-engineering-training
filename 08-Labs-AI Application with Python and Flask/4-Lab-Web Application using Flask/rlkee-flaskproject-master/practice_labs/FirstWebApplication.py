from flask import Flask

app = Flask("First Flask Application")


@app.route("/")
def hello():
    return "Hello Flask"


if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000