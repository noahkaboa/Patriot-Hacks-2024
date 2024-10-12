from flask import Flask, render_template # pip install flask
import nlp

app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)