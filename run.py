from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    """
    Creates tables before first request if they don't exist
    """
    db.create_all()