height = float (input("Your height (cm): "))/100
weight = int (input("Your weight (kg): "))
BMI = weight/ (height * height)
if BMI < 16:
    print ("Severely underweight")
elif BMI < 18.5:
    print ("Underweight")
elif BMI < 25:
    print ("Normal")
elif BMI < 30:
    print ("Overweight")
else:
    print ("Obese")