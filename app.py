from flask import Flask
from flask import request
import ast
app = Flask(__name__)
def example_func(a):
    print(a)

@app.route('/calc',methods=['GET'])
def calc():
    value = request.args['value']
    pattern = ast.literal_eval(value)
    example_func(pattern)
    return 'This is my first API call!'