from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # print the hostname to verify we are running inside the container/VM
    return f"Hello from Python Agent! Running on: {socket.gethostname()}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)