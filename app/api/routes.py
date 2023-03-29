from flask import Blueprint, request, jsonify, render_template
import sqlalchemy
from helpers import token_required
from models import db, User, Recipe, Exercise, Log, recipe_schema, recipes_schema, exercise_schema, exercises_schema, log_schema, logs_schema

api = Blueprint('api', __name__, url_prefix='/api')

# RECIPES SECTION
@api.route('/recipes', methods = ['POST'])
@token_required
def create_recipe(current_user_token):
    name = request.json['name']
    meal = request.json['meal']
    ingridients = request.json['ingridients']
    full_recipe = request.json['full_recipe']
    user_token = current_user_token.token  

    recipe = Recipe(name, meal, ingridients, full_recipe, user_token = user_token)

    db.session.add(recipe)
    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)

@api.route('/recipes', methods = ['GET'])
@token_required
def get_recipes(current_user_token):
    a_user = current_user_token.token
    recipes = Recipe.query.filter_by(user_token = a_user).all()
    response = recipes_schema.dump(recipes)
    return jsonify(response)

@api.route('/recipes/<id>', methods = ['GET'])
@token_required
def get_single_recipe(current_user_token, id):
    recipe = Recipe.query.get(id)
    response = recipe_schema.dump(recipe)
    return jsonify(response)

@api.route('/recipes/<id>', methods = ['POST', 'PUT'])
@token_required
def update_recipe(current_user_token, id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.meal = request.json['meal']
    recipe.ingridients = request.json['ingridients']
    recipe.full_recipe = request.json['full_recipe']
    recipe.user_token = current_user_token.token  

    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)


@api.route('/recipes/<id>', methods = ['DELETE'])
@token_required
def delete_recipe(current_user_token, id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)



# EXERCISES SECTION
@api.route('/exercises', methods = ['POST'])
@token_required
def create_exercise(current_user_token):
    name = request.json['name']
    muscle = request.json['muscle']
    type_exercise = request.json['type_exercise']
    difficulty = request.json['difficulty']
    description = request.json['description']
    user_token = current_user_token.token  

    exercise = Exercise(name, muscle, type_exercise, difficulty, description, user_token = user_token)

    db.session.add(exercise)
    db.session.commit()
    response = exercise_schema.dump(exercise)
    return jsonify(response)


@api.route('/exercises', methods = ['GET'])
@token_required
def get_exercises(current_user_token):
    a_user = current_user_token.token
    exercises = Exercise.query.filter_by(user_token = a_user).all()
    response = exercises_schema.dump(exercises)
    return jsonify(response)

@api.route('/exercises/<id>', methods = ['GET'])
@token_required
def get_single_exercise(current_user_token, id):
    exercise = Exercise.query.get(id)
    response = exercise_schema.dump(exercise)
    return jsonify(response)

@api.route('/exercises/<id>', methods = ['POST', 'PUT'])
@token_required
def update_exercise(current_user_token, id):
    exercise = Exercise.query.get(id)
    exercise.name = request.json['name']
    exercise.muscle = request.json['muscle']
    exercise.type_exercise = request.json['type_exercise']
    exercise.difficulty = request.json['difficulty']
    exercise.description = request.json['description']
    exercise.user_token = current_user_token.token  

    db.session.commit()
    response = exercise_schema.dump(exercise)
    return jsonify(response)

@api.route('/exercises/<id>', methods = ['DELETE'])
@token_required
def delete_exercise(current_user_token, id):
    exercise = Exercise.query.get(id)
    db.session.delete(exercise)
    db.session.commit()
    response = exercise_schema.dump(exercise)
    return jsonify(response)

# LOGS SECTION
@api.route('/logs', methods = ['POST'])
@token_required
def create_log(current_user_token):
    date = request.json['date'] 
    weight = request.json['weight']
    sleep = request.json['sleep']
    steps = request.json['steps']
    work_out = request.json['work_out']
    user_token = current_user_token.token  

    log = Log(date, weight, sleep, steps, work_out, user_token = user_token)

    db.session.add(log)
    db.session.commit()
    response = log_schema.dump(log)
    return jsonify(response)

@api.route('/logs', methods = ['GET'])
@token_required
def get_logs(current_user_token):
    a_user = current_user_token.token
    logs = Log.query.filter_by(user_token = a_user).all()
    response = logs_schema.dump(logs)
    return jsonify(response)

@api.route('/logs/<id>', methods = ['GET'])
@token_required
def get_single_log(current_user_token, id):
    log = Log.query.get(id)
    response = log_schema.dump(log)
    return jsonify(response)

@api.route('/logs/<id>', methods = ['POST', 'PUT'])
@token_required
def update_log(current_user_token, id):
    log = Log.query.get(id)
    log.date = request.json['date']
    log.weight = request.json['weight']
    log.sleep = request.json['sleep']
    log.steps = request.json['steps']
    log.work_out = request.json['work_out']
    log.user_token = current_user_token.token  

    db.session.commit()
    response = log_schema.dump(log)
    return jsonify(response)


@api.route('/logs/<id>', methods = ['DELETE'])
@token_required
def delete_log(current_user_token, id):
    log = Log.query.get(id)
    db.session.delete(log)
    db.session.commit()
    response = log_schema.dump(log)
    return jsonify(response)