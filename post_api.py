from flask import Flask,jsonify
from post1 import Piece
import requests


app = Flask(__name__)
@app.route('/home')
def home():
    payload = {'slackUsername': 'Miracle Igwe',
                'operation_type': Piece.enum.value,
                }

    r = requests.post('https://httpbin.org/post', data=payload)
    
    my_Sum = Piece.x.value + Piece.y.value
    payload["result"] = my_Sum
    print(payload)

    return jsonify(payload)    

    



if __name__ == '__main__':
    app.run(debug=True)