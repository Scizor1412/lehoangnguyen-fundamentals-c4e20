from flask import Flask, render_template
import mlab
from mongoengine import *
from models.service import Service

app = Flask(__name__)
mlab.connect()

# Design pattern(ModelsViewController, MVP, MVPP)
#Design database

@app.route('/search/<g>')
def search(g):
    
    all_service = Service.objects(
        gender = g,
        yob__lte=1998,
        height__gt=165,
        address__icontains='Hà Nội')
    return render_template(
        'search.html',
        all_service=all_service
        )

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 