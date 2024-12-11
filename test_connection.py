from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Supu@localhost:5432/blog_db'
db = SQLAlchemy(app)

try:
    with app.app_context():
        # Use connection to execute a raw SQL statement
        with db.engine.connect() as connection:
            result = connection.execute(db.text("SELECT 1"))  # Correct way to execute raw SQL in SQLAlchemy 2.x
            print("Database connection successful!")
except Exception as e:
    print("Database connection failed:", e)
