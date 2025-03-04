from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is a Flask app running in a Docker container."

if __name__ == '__main__':
    app.run(host='192.168.100.22', port=5000)