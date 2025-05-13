from flask import Flask, render_template
from dict_data import get_definition

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dictionaryapi/v1/<word>')
def api(word):
    return {'word': word,
           'definition': get_definition(word)}


if __name__ == '__main__':
    app.run(debug=True)