from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    
    # BMI categories
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal/Healthy"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

@app.route('/')
def home():
    return "BMI App is running! Use POST /bmi to calculate BMI."

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    
    if not data or 'weight' not in data or 'height' not in data:
        return jsonify({"error": "Please provide weight (kg) and height (m)"}), 400
    
    weight = float(data['weight'])
    height = float(data['height'])
    
    bmi_value, category = calculate_bmi(weight, height)
    
    return jsonify({
        "weight": weight,
        "height": height,
        "bmi": bmi_value,
        "category": category
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


