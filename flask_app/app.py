from flask import Flask, render_template # pip install flask
import nlp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start-page')
def start_page():
    return render_template('start-page.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)