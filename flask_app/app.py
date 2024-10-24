import traceback
from flask import Flask, render_template, request, redirect, url_for, jsonify, current_app, flash # pip install flask
import nlp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start-page')
def start_page():
    return render_template('start-page.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json(silent=True)
        if not data or 'interests' not in data:
            return jsonify({'error': 'Invalid request'}), 400
        array = data.get('interests', [])

        recommendations = nlp.rank_businesses(array, 5)
        print(f"recommendations: {recommendations}")

        return jsonify({'recommendations': recommendations})
    except Exception as e:
        print(f"Error: {e}")
        print(f"Error: {traceback.format_exc()}")
        return jsonify({'error': str(e)}), 500

@app.route('/your-day/<result_array>')
def your_day(result_array):
    try:
        businesses = result_array.split(',')

        return render_template('your-day.html', businesses=businesses, descriptions=[nlp.get_desc(business) for business in businesses], zip=zip)
    except Exception as e:
        print(f"Error: {e}")
        return redirect(url_for('home'))


print("??")
if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True, host='127.0.0.1', port=5000)