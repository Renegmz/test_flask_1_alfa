from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return {
        "payload":"welcome to my project"
    }

@app.route("/read")
def read():
    return {"payload":"read successfully"
    }

@app.route("/create", methods=["POST"])
def create():
    return {"payload":"create successfully"
    }

@app.route("/delete", methods=["DELETE"])
def create():
    return {"payload":"delete successfully"
    }

if __name__ == '__main__':
    app.run(debug=True)

