from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# [API-02] Configure the SQLite database
# This will create a file named 'mini_management.db' in your root folder later
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mini_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database tool
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "API-02: Database connection configured!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)