import json
from operator import index
from flask import Flask, jsonify, request

app = Flask(__name__)
temp=[
    {
        "id" : "0",
        "date": "10/04/2022",
        "temperature": "36"
    },
    {
        "id" : "1",
        "date": "10/03/2022",
        "temperature": "37"
    },
]
@app.route('/temp',methods=['POST'])
def insert():
    added = request.get_json()
    temp.append(added)
    return {'id':len(temp)},200

@app.route('/temp', methods=['GET'])
def read():
    return jsonify(temp)

@app.route('/temp/<string:id>')
def specific(id):
    for x in temp:
        if (x['id']==id):
            return jsonify(x)
    return jsonify({'text':'Invalid ID'})

@app.route('/temp/<int:index>', methods=['PUT'])
def update(index):
    updateTemp = request.get_json()
    temp[index] = updateTemp
    return jsonify(temp[index])

@app.route('/temp/<int:index>',methods=['DELETE'])
def delete(index):
    temp.pop(index)
    return 'Record was successfully deleted',200


if __name__ == '__main__':
    app.run()
