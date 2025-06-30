from flask import Flask

app = Flask("FlowPrep")

@app.route('/')
def index():
    return "Hello World"


if __name__== "__main__":
    app.run(debug=True)