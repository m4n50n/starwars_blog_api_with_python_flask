from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return "<User %r>" % f"id: {self.id}"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,          
            "created_at": self.created_at
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    temperature = db.Column(db.Float)
    image_url = db.Column(db.String(250))
    
    def __repr__(self):
        return "<Planet %r>" % f"id: {self.id}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "temperature": self.temperature,
            "image_url": self.image_url            
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500))
    birthday = db.Column(db.DateTime)
    image_url = db.Column(db.String(250))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship(Planet)

    def __repr__(self):
        return "<Character %r>" % f"id: {self.id}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "birthday": self.birthday,
            "image_url": self.image_url,
            "planet_id": self.planet_id
        }

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    character = db.relationship(Character)
    planet = db.relationship(Planet)

    def __repr__(self):
        return "<Favourite %r>" % f"id: {self.id}"

    def serialize(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }
