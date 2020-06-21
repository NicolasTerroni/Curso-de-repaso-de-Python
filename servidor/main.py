from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "AL FIN UN POCO DE BACKEND"

if __name__ == "__main__":
    app.run()