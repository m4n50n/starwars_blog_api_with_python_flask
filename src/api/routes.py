"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Planet, Character, Favourite
from api.utils import generate_sitemap, APIException

api = Blueprint("api", __name__)

#region Users
# Add user
@api.route("/user/add", methods=["POST"]) # "/api/user/add"
def add_user():
    body = request.get_json()
    new_user = User(email=body["email"], password=body["password"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(f"A new user is added: {new_user.serialize()}"), 200

# Get all users
@api.route("/user/get/", methods=["GET"])
def get_all_users():
    u = User() # Create new class instance
    return jsonify(u.get_all_users()), 200

# Get user
@api.route("/user/get/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)

    if user == None:
        response = f"There is no user with ID '{user_id}'"
    else:
        response = user.serialize()

    return jsonify(response), 200
#endregion Users

#region Planets
# Get all planets
@api.route("/planet/get/", methods=["GET"])
def get_all_planets():
    p = Planet()
    return jsonify(p.get_all_planets()), 200

# Get planet
@api.route("/planet/get/<int:planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet == None:
        response = f"There is no planet with ID '{planet_id}'"
    else:
        response = planet.serialize()

    return jsonify(response), 200
#endregion Planets

#region Characters
# Get all character
@api.route("/character/get/", methods=["GET"])
def get_all_characters():
    c = Character()
    return jsonify(c.get_all_characters()), 200

# Get character
@api.route("/character/get/<int:character_id>", methods=["GET"])
def get_character(character_id):
    character = Character.query.get(character_id)

    if character == None:
        response = f"There is no character with ID '{character_id}'"
    else:
        response = character.serialize()

    return jsonify(response), 200
#endregion Characters

#region Favourites
# Add favourite
@api.route("/user/favourite/add/", methods=["POST"])
def add_favourite():
    body = request.get_json()

    if body["type"] == "character":
        new_favourite = Favourite(user_id=body["user_id"], character_id=body["character_id"])
    elif body["type"] == "planet":
        new_favourite = Favourite(user_id=body["user_id"], planet_id=body["planet_id"])
       
    db.session.add(new_favourite)
    db.session.commit()

    return jsonify(f"A new favourite is added: {new_favourite.serialize()}"), 200

# Get all favourites
@api.route("/user/favourite/get/<int:user_id>", methods=["GET"])
def get_all_favourites(user_id):
    c = Favourite()
    return jsonify(c.get_all_favourites(user_id)), 200

# Delete favourite
@api.route("/user/favourite/delete/<int:favourite_id>", methods=["DELETE"])
def delete_favourite(favourite_id):
    favourite = Favourite.query.get(favourite_id)

    if favourite == None:
        return f"There is no favourite with ID '{favourite_id}'"
    else:
        Favourite.query.filter_by(id=favourite_id).delete()
        db.session.commit()

        return jsonify(f"Favourite with ID '{favourite_id}' has been deleted!!"), 200 
#endregion Favourites