from app import app
from models import db,Update

with app.app_context():
    print Update.query.all()