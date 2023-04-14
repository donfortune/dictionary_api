from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/api/v1/<word>')

def api(word):
    definition = word.upper()
    output = {'definition': definition, 'word': word }
    return output

app.run(debug=True)