from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return """Go to /bmi/weight/height to have your BMI calculated
    Note that height are in centimeter"""

# @app.route('/bmi/<int:weight>/<int:height>')
# def BMI_calculator(weight,height):
#     BMI = weight*100*100/(height**2)
#     if BMI < 16:
#         return "Severely underweight"
#     elif BMI < 18.5:
#         return "Underweight"
#     elif BMI < 25:
#         return "Normal"
#     elif BMI < 30:
#         return "Overweight"
#     else:
#         return "Obese"

@app.route('/bmi/<int:weight>/<int:height>')
def BMI_calculator(weight, height):
    BMI = weight*10000/(height)**2
    return render_template ('BMI.html', BMI = BMI)

if __name__ == '__main__':
  app.run(debug=True)
 