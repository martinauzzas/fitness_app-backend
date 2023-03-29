from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String, nullable = True, default = "")
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = "", unique = True)
    data_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, password = "", token = "", g_auth_verify = False):
        self.id = self.set_id()
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User { self.email } has been added'

# I want to have a database for the recipes, exercises and daily logs
# So I'll need different class so I can insert that data into my database

# Then on the react app I can create different form for the 3 different databases in 
# order to add the data into the right section

class Recipe(db.Model):
    id = db.Column(db.String, primary_key= True)
    name = db.Column(db.String(200), nullable = False)
    meal = db.Column(db.String(100))
    ingridients = db.Column(db.String(500))
    full_recipe = db.Column(db.String(1000))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, meal, ingridients, full_recipe, user_token, id = ''):
        self.id = self.set_id()
        self.name = name
        self.meal = meal
        self.ingridients = ingridients
        self.full_recipe = full_recipe
        self.user_token = user_token


    def __repr__(self):
        return f'Recipe: {self.name} added'

    def set_id(self):
        return (secrets.token_urlsafe())
    
class RecipeSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'meal', 'ingridients', 'full_recipe']

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many= True)

class Exercise(db.Model):
    id = db.Column(primary_key= True)
    name = db.Column(db.String(200), nullable = False)
    muscle = db.Column(db.String(100))
    type_exercise = db.Column(db.String(500))
    difficulty = db.Column(db.String(100))
    description = db.Column(db.String(500))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, muscle, type_exercise, difficulty, description, user_token, id= ''):
        self.id = self.set_id()
        self.name = name
        self.muscle = muscle
        self.type_exercise = type_exercise
        self.difficulty = difficulty
        self.description = description
        self.user_token = user_token

    def __repr__(self):
        return f'Exercise: {self.name} added'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class ExerciseSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'muscle', 'type_exercise', 'difficulty', 'description']

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many= True)

class Log(db.Model):
    id = db.Column(primary_key= True)
    date = db.Column(db.String(100))
    weight = db.Column(db.String(10))
    sleep = db.Column(db.String(10))
    steps = db.Column(db.Integer()) #TODO: CHECK INTEGER if it works
    work_out = db.Column(db.String(500))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, date, weight, sleep, steps, work_out, user_token, id= ''):
        self.id = self.set_id()
        self.date = date
        self.weight = weight
        self.sleep = sleep
        self.steps = steps
        self.work_out = work_out
        self.user_token = user_token


    def __repr__(self):
        return f"{self.date}'s log added"
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
    
class LogSchema(ma.Schema):
    class Meta:
        fields = ['id', 'date', 'weight', 'sleep', 'steps', 'work_out']

log_schema = LogSchema()
logs_schema = LogSchema(many= True)