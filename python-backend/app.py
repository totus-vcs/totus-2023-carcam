# FLASK API
from flask import Flask, jsonify, request
from flask_cors import CORS


# FLASK APP
app = Flask(__name__)
CORS(app)

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
# @app.route('/home/<int:num>', methods = ['GET'])
# def disp(num):
  
#     return jsonify({'data': num**2})

# SCHEMA
@app.route('/test')
def test(): 
    return jsonify(True)


# MAIN
if __name__ == '__main__':
  
    app.run(debug = True, host='0.0.0.0')# FLASK API
