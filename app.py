from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "Aplicación en CI/CD con Jenkins y Docker"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)
