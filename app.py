from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "API-01: Flask server is running..."

if __name__ == '__main__':
    app.run(debug=True, port=5000)