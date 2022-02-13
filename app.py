from flask import Flask
import flowerDB as flower
# import data_houses as houses
from flask import jsonify

app = Flask(__name__)



@app.route('/gp')
def index():
    responce = flower.output_all()
    return jsonify(responce)


@app.route('/anw')
    responce = flower.add_new_order()
    return jsonify(responce)





@app.route('/hello') # Routes you to the page with http://127.0.0.1:5000/hello/
def hello():
    return 'Hello, World'

@app.route('/projects/') # URL with trailing slash
def projects():
    return 'The project page'

@app.route('/about') # URL without a trailing slash
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(host='0.0.0.0')