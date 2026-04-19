from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    # Relationship: A user owns many workouts
    workouts = db.relationship('Workout', back_populates='user', cascade='all, delete-orphan')

    serialize_rules = ('-_password_hash', '-workouts',)

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)

class Workout(db.Model, SerializerMixin):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String, nullable=False)
    duration_minutes = db.Column(db.Integer)
    intensity = db.Column(db.String) 
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='workouts')

    serialize_rules = ('-user',)

    @validates('exercise')
    def validate_exercise(self, key, value):
        if not value or len(value) < 2:
            raise ValueError("Exercise name must be at least 2 characters.")
        return value


