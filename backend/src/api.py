import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from functools import wraps
from jose import jwt
import json
from flask_cors import CORS
from urllib.request import urlopen

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app,resources={r"/*":{"origins":'*'}})

# CORS setup
@app.after_request
def after_request(response):
  #response.
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

'''
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
db_drop_and_create_all()

# Because there is no drink in the database,
# Add a mock beverage
recipe= [{
  "name": "Cola",
  "color": "Black",
  "parts": 1
    }]
new_drink = Drink(title='Cola', recipe=json.dumps(recipe))
new_drink.insert()

## ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/')
def index_page():
  return ('Coffee shop powered by Hellogaga')

@app.route('/drinks')
def coffee():
  '''
  endpoint for get all drinks
  No permission required
  '''
  # get all drinks
  drinks = Drink.query.all()
  
  # abort if no data 
  if len(drinks) == 0:
    abort(404)

  # make a list to hold the outout data
  drinks_list = []
  for drink in drinks_list:
    drinks_list.append(drink.short())
  
  # return a json
  return jsonify({
    'success':True,
    'drinks':drinks_list
  }),200


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drink_detail(jwt_token):
  '''
  Endpoint for get all drink details. 
  Permission is checked.
  '''

  # get all drinks
  drinks = Drink.query.all()
  
  # abort if no data 
  if len(drinks) == 0:
    abort(404)

  # make a list to hold the outout data
  drinks_list = []
  for drink in drinks_list:
    drinks_list.append(drink.long())
  
  # return a json
  return jsonify({
    'success':True,
    'drinks':drinks_list
  }),200


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_a_new_drink(jwt_token):
  '''
  Endpoint for create a new drink. 
  Permission is checked.
  '''
  # check input data
  data = request.get_json()
  if 'title' and 'recipe' not in data:
    abort(422)
  
  # Insert the new drink
  title = data['title']
  recipe_json = json.dumps(data['recipe'])
  drink = Drink(title=title, recipe=recipe_json)
  drink.insert()
  
  # return message
  return jsonify({
      'success': True,
      'drinks': [drink.long()]
  })


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('post:drinks')
def patch_a_drink(jwt_token,id):
  '''
  Endpoint for revise a new drink. 
  Permission is checked.
  '''
  # check if drink exists
  drink = Drink.query.get(id)
  if drink is None:
      abort(404)
  
  # check the input data
  data = request.get_json()
  if 'title' in data:
      drink.title = data['title']
  if 'recipe' in data:
      drink.recipe = json.dumps(data['recipe'])
  
  # update the drink
  drink.update()

  return jsonify({
      'success': True,
      'drinks': [drink.long()]
  })


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('post:drinks')
def delete_a_drink(jwt_token,id):
  '''
  Endpoint for delete a drink. 
  Permission is checked.
  '''
  # check if drink exists
  drink = Drink.query.get(id)
  if drink is None:
      abort(404)

  # if exists, delete
  drink.delete()
  
  # return message
  return jsonify({
      'success': True,
      'delete': drink.id
  })

## Error Handling
'''
error handling for 422 404 400 403 500 401
'''
@app.errorhandler(422)
def unprocessable(error):
  return jsonify({
    "success": False, 
    "error": 422,
    "message": "unprocessable"
    }), 422

@app.errorhandler(401)
def unauthorized(error):
  return jsonify({
    "success": False, 
    "error": 401,
    "message": "unauthorized"
    }), 401


@app.errorhandler(404)
def not_found(error):
  return jsonify({
      'success': False,
      'error': 404,
      'message': 'resource not found'
  }), 404

'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''
@app.errorhandler(400)
def bad_request(error):
  return jsonify({
      'success': False,
      'error': 400,
      'message': 'Bad request error'
  }), 400

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''

@app.errorhandler(500)
def internal_server_error(error):
  return jsonify({
      'success': False,
      'error': 500,
      'message': 'An internal error has occured'
  }), 500

@app.errorhandler(403)
def no_authorization(error):
  return jsonify({
      'success': False,
      'error': 403,
      'message': 'not authorized'
  }), 403

@app.errorhandler(AuthError)
def process_AuthError(error):
  response = jsonify(error.error)
  response.status_code = error.status_code

  return response