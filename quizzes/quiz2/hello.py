from flask import Flask
from flask import request
from flask import jsonify,json
app = Flask(__name__)

usersList = []
userNo = 0


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/users', methods=['POST'])
def users():
    name = request.form["name"]
    global userNo
    userNo += 1
    user = {
        'id' : userNo,
        'name' : name
    }
    usersList.append(user) 
    return json.dumps(user, indent=4, separators=(',', ':')), 201

@app.route('/users/<userid>')
def getUsers(userid):
    userName = ''
    for i in range(len(usersList)):
        if(int(usersList[i]['id']) == int(userid)):
            userName = str(usersList[i]['name'])
            user = {
            'id' : userid,
            'name' : userName
            }
        else:
            user = {
                'message' : 'User with given userid isnt available'
            }
    return json.dumps(user, indent=4, separators=(',', ':'))

@app.route('/users/<userid>', methods=['DELETE'])
def deleteUsers(userid):
    userName = ''
    for i in range(len(usersList)):
        if(int(usersList[i]['id']) == int(userid)):
            userName = str(usersList[i]['name'])
            user = {
                'id' : userid,
                'name' : userName
            }
            usersList.pop(i)
            break
        else:
            user = {
                'message' : 'User with given userid cannot be deleted'
            }
    return '', 204

