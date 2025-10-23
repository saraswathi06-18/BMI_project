from flask import Flask, request, jsonify

app = Flask(__name__)

# GET route to test if app is running
@app.route('/')
def home():
    return "BMI App is running! Use POST /bmi to calculate BMI."

# POST route to calculate BMI
@app.route('/bmi', methods=['POST'])
def calculate_bmi():
    try:
        data = request.get_json()
        weight = float(data['weight'])   # in kg
        height = float(data['height'])   # in meters

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = 'Underweight'
        elif bmi < 24.9:
            status = 'Normal'
        elif bmi < 29.9:
            status = 'Overweight'
        else:
            status = 'Obese'

        return jsonify({'bmi': round(bmi, 2), 'status': status})
    
    except Exception as e:
        return jsonify({'error': 'Invalid input', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
