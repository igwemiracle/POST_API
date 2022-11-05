from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def operation():
  operation_type = request.json['operation_type']
  x = request.json['x']
  y = request.json['y']
  if(operation_type == 'addition'):
    result = x + y
  elif(operation_type == 'subtraction'):
    result = x - y
  elif(operation_type == 'multiplication'):
    result = x * y
  payload = {'slackUserName': 'Miracle','operation_type': operation_type, 'result':result }
  return jsonify(payload)


app.run()