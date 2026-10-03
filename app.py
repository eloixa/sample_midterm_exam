from flask import Flask
from database import db
from models import User, Record

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mini_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect the db to this specific app
db.init_app(app)

# Generate the actual database file and tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "API-03: Database tables created successfully!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)