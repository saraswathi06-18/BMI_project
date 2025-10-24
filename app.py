from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal/Healthy"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category

@app.route('/')
def home():
    return render_template('index.html')  # will create this next

@app.route('/bmi', methods=['POST'])
def bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi_value, category = calculate_bmi(weight, height)
    return render_template('result.html', bmi=bmi_value, category=category, weight=weight, height=height)

if __name__ == "__main__":
    app.run(debug=True)
