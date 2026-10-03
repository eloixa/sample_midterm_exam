from flask import Flask, request, jsonify
from database import db, bcrypt
from models import User, Record

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mini_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize tools
db.init_app(app)
bcrypt.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Check if user already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({"message": "Username already exists"}), 400

    # Hash the password securely
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    
    # Create and save the new user
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)