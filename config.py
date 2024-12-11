class Config:
    # Database URI (use your own username, password, and db name)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Supu@localhost:5432/blog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for performance

    #Your other configurations...
    SECRET_KEY = 'a_random_secret_key' #you can replace this with a more secure key

