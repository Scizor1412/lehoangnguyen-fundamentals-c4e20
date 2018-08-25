from flask import Flask, render_template
import mlab
from mongoengine import *
from Models.client import Client
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete-all-client')
def delete_all():
    all_client = Client.objects()
    while len(all_client) > 0:
        all_client[0].delete()
    return 'Deleted'

@app.route('/search')
def search():
    all_client = Client.objects()
    return render_template(
        'search.html',
        all_client = all_client
        )

@app.route("/detail/<id>")
def detail(id):
    client = Client.objects.with_id(id)
    return render_template ('detail.html', client = client)
    
if __name__ == '__main__':
  app.run(debug=True)