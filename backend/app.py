from flask import Flask # pip install flask
import nlp

app = Flask(__name__)

@app.route('/')
def index():
    pass



if __name__ == '__main__':
    app.run(debug=True)