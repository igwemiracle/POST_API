from flask import Flask, jsonify, request
from enums import Operations


app = Flask(__name__)

@app.route("/", methods=["POST"])
def operation():
  operation_type = request.json['operation_type']
  x = request.json['x']
  y = request.json['y']
  if(operation_type == Operations.ADDITION.value):
    operation_result = x + y
  elif(operation_type == Operations.SUBTRACTION.value):
    operation_result = x - y
  elif(operation_type == Operations.MULTIPLICATION.value):
    operation_result = x * y
  payload = {'slackUsername': 'Miracle','operation_type': operation_type, 'result':operation_result }
  return jsonify(payload)


if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')