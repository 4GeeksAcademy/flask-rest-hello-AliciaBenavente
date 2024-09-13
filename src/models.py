from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }

# class Gender(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     gender = db.Column(db.String(120), nullable=False)

#     def __repr__(self):
#         return '<Gender %r>' % self.gender

#     def serialize(self):
#         return {
#             "id": self.id,
#             "gender": self.gender,
#         }

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
    name = db.Column(db.String(120), nullable=False)
    species = db.Column(db.String(120), nullable=True)
    homeplanet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    homeplanet = db.relationship(Planets)
    gender_id = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "homeplanet_id": self.homeplanet_id,
            "gender": self.gender_id,
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    creation_date = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=False)
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

    


# class Login(db.Model):
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     planets_id = Column(Integer, ForeignKey('planets.id'))
#     characters_id = Column(Integer, ForeignKey('characters.id'))
#     person = relationship(User)



# def to_dict(self):
#     return {}