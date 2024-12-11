from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the database and migration instances
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Set the SECRET_KEY for session management
    app.config['SECRET_KEY'] = 'a_random_secret_key'  # Replace this with a secure key

    #Configuring database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Supu@localhost:5432/blog_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disable modification tracking for performance

    # Load configuration from config.py
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and initialize routes here
    from .routes import init_routes
    init_routes(app) # Initialize routes with the app instance

    return app
