import os
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
        return 'Rota com problema {}'.format(request.url), 404

@app.route("/")
@app.route("/index")
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
