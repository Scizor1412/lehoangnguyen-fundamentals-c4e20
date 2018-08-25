from flask import *
import mlab
from mongoengine import *
from models.service import Service

app = Flask(__name__)
mlab.connect()

# Design pattern(ModelsViewController, MVP, MVPP)
#Design database

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects()
    return render_template(
        'search.html',
        all_service=all_service
        )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template(
        'admin.html',
        all_service=all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    delete_service = Service.objects.with_id(service_id)
    if delete_service is not None:
        delete_service.delete()
        return redirect(url_for('admin'))
    else:
        return "Not Found"
    
@app.route('/delete-all-service')
def delete_all_service():
    all_service = Service.objects()
    while len(all_service) > 0:
        all_service[0].delete()
    return 'Deleted'

@app.route('/new-service', methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        if form['gender'] == 'male':
            gender = 1
        else:
            gender = 0
        new_service = Service(
            name=name,
            yob=yob,
            phone=phone,
            gender=gender
        )
        new_service.save()

        return redirect(url_for('admin'))

@app.route('/edit/<id>', methods = ["GET", "POST"])
def edit(id):
    edit_service = Service.objects.with_id(id)
    if edit_service is not None:
        if request.method == "GET":
            return render_template('edit-service.html', service = edit_service)
        elif request.method == "POST":
            form = request.form
            name = form['name']
            yob = form ['yob']
            phone = form ['phone']
            if form['gender'] == 'male':
                gender = 1
            else:
                gender = 0
            edit_service = Service.update(
                set__name=name,
                set__yob=yob,
                set__phone=phone,
                set__gender=gender)
    else:
        return "Not Found"


@app.route('/detail/<id>')
def detail(id):
    service = Service.objects.with_id (id)
    return render_template('detail.html', service = service)

if __name__ == '__main__':
  app.run(debug=True)
 