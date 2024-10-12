from flask import Flask, render_template # pip install flask
import nlp

app = Flask(__name__)

@app.route('/')
def index():
    render_template('home/index.html')

@app.route('/start-page')
def start_page():
    return render_template('start-page/index.html')



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)