from bson import ObjectId
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
cors = CORS(app)
app.config['MONGO_DBNAME'] = 'v-todo'
app.config['MONGO_URI'] = 'mongodb://vs:e1392781@ds163700.mlab.com:63700/v-todo'
mongo = PyMongo(app)


@app.route('/todo', methods = ['GET'])
def get_all_todo():
    todo = mongo.db.todo
    response = []
    for i in todo.find():
        _dict = {
            'id': str(i['_id']),
            'name': i['name'],
            'finished': i['finished'],
            'favourite': i['favourite']
        }
        response.append(_dict)
    return jsonify({'data': response})


@app.route('/todo', methods = ['POST'])
def create_todo():
    collection = mongo.db.todo
    _dict = {
        'name': request.json['name'],
        'finished': request.json['finished'],
        'favourite': request.json['favourite']
    }
    collection.insert(_dict)
    response = []
    for i in collection.find():
        _dict = {
            'id': str(i['_id']),
            'name': i['name'],
            'finished': i['finished'],
            'favourite': i['favourite']
        }
        response.append(_dict)
    return jsonify({'data': response})


@app.route('/todo', methods = ['PUT'])
def update_todo():
    collection = mongo.db.todo
    _dict = {
        'name': request.json['name'],
        'finished': request.json['finished'],
        'favourite': request.json['favourite']
    }
    response = []
    collection.find_one_and_update({'_id': ObjectId(request.json['id'])}, {'$set': _dict})
    for i in collection.find():
        _dict = {
            'id': str(i['_id']),
            'name': i['name'],
            'finished': i['finished'],
            'favourite': i['favourite']
        }
        response.append(_dict)
    return jsonify({'data': response})


@app.route('/todo/<t_id>', methods = ['DELETE'])
def delete_todo(t_id):
    collection = mongo.db.todo
    collection.delete_one({'_id': ObjectId(t_id)})
    response = []
    for i in collection.find():
        _dict = {
            'id': str(i['_id']),
            'name': i['name'],
            'finished': i['finished'],
            'favourite': i['favourite']
        }
        response.append(_dict)
    return jsonify({'data': response})


if __name__ == '__main__':
    app.run()
