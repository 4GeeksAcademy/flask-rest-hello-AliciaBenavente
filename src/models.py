from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

db = SQLAlchemy()


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    region = db.Column(db.String(120), nullable=True)
    sector = db.Column(db.String(120), nullable=True)
    system = db.Column(db.String(120), nullable=True)
    inhabitants = db.Column(db.Integer, nullable=True)
    capital_city = db.Column(db.String(120), nullable=True)
    coordinates = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "region": self.region,
            "sector": self.sector,
            "system": self.system,
            "inhabitants": self.inhabitants,
            "capital_city": self.capital_city,
            "coordinates": self.coordinates,
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    species = db.Column(db.String(120), nullable=True)
    homeplanet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    homeplanet = db.relationship(Planets)
    gender = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "homeplanet_id": self.homeplanet_id,
            "gender": self.gender,
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    creation_date = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "active": self.is_active,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = db.relationship(User)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    characters = db.relationship(Characters)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets = db.relationship(Planets)
    
    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "planets_id": self.planets_id,  
            "characters_id": self.characters_id,              
        }

class Favorite_Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    description = db.Column(db.String(200), nullable=True)
    
    def __repr__(self):
        return '<Favorite_character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "characters_id": self.characters_id,
            "description" : self.description,           
        }

class Favorite_Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    description = db.Column(db.String(200), nullable=True)
    
    def __repr__(self):
        return '<Favorite_planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "planets_id": self.planets_id,
            "description" : self.description,           
        }

# class Login(db.Model):
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     planets_id = Column(Integer, ForeignKey('planets.id'))
#     characters_id = Column(Integer, ForeignKey('characters.id'))
#     person = relationship(User)



# def to_dict(self):
#     return {}