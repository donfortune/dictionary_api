from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
data = pd.read_csv('dictionary.csv')
@app.route('/')

def home():
    return render_template('index.html')

@app.route('/api/v1/<word>')

def api(word):
    definition = data.loc[data['word'] == word]['definition'].squeeze()
    results = {'word': word, 'definition': definition}
    return results

app.run(debug=True)