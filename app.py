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

if __name__ == '__main__':
    app.run(debug=True)
