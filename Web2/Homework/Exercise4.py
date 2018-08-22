from flask import Flask, render_template
from models.customer import Customer
import mlab
from mongoengine import *

app = Flask(__name__)

mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first_male')
def first_male():
    male_customer = Customer.objects(
        gender = 1,
    )
    return render_template(
        'first_male.html',
        male_customer = male_customer[0:10])

@app.route('/customer/')
def search():
    
    all_customer = Customer.objects()
    return render_template(
        'customer.html',
        all_customer=all_customer
        )

if __name__ == '__main__':
  app.run(debug=True)