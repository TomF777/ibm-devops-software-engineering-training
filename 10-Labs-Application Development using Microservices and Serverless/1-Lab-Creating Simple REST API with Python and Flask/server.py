from flask import Flask

app = Flask("My Hello World Application")

@app.route("/")
def hello():
    return "Hello Flask"


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)

