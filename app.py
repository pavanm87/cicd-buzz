import os
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
        return 'Rota com problema {}'.format(request.url), 404

@app.route("/buzz")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

@app.route("/name")
def generate_name():
    page = '<html><body><h1>'
    page += Hi I Am Pavan.
    page += '</h1></body></html>'
    return page

@app.route("/")
@app.route("/index")
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
