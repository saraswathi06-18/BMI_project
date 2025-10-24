from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>BMI Calculator</h2>
        <form method="POST" action="/bmi">
            Weight (kg): <input type="number" step="0.1" name="weight" required><br><br>
            Height (m): <input type="number" step="0.01" name="height" required><br><br>
            <input type="submit" value="Calculate BMI">
        </form>
    '''

@app.route('/bmi', methods=['POST'])
def bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi_value = weight / (height ** 2)
    
    return f'''
        <h2>Your BMI is: {bmi_value:.2f}</h2>
        <a href="/">Calculate Again</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
