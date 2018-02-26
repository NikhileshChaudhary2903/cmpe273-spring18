from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

users = [{'id': 1, 'name': u'Leo Messi'}, {'id': 2,
         'name': u'Cristiano Ronaldo'}]


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/users/<int:user_id>', methods=['GET', 'DELETE'])
def get_user(user_id):
    if request.method == 'GET':
        user = [user for user in users if user['id'] == user_id]
        if len(user) == 0:
            abort(404)
        return (jsonify({'user': user[0]}), 200)
    elif request.method == 'DELETE':

        user = [user for user in users if user['id'] == user_id]
        if len(user) == 0:
            abort(404)
        users.remove(user[0])
        return (jsonify({'result': True}), 204)


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = {'id': users[-1]['id'] + 1, 'name': request.json['name']}
    users.append(user)
    return (jsonify({'user': user}), 201)
