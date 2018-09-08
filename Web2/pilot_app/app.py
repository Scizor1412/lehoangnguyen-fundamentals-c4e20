from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.user import User
from models.order import Order
from datetime import datetime

app = Flask(__name__)
app.secret_key = "a super super super super secret key"
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
        height = form['height']
        address = form['address']
        description = form['description']
        image = form['image']
        measurements = form['measurements'].split('-')
        if form['gender'] == 'male':
            gender = 1
        else:
            gender = 0
        
        new_service = Service(
            name=name,
            yob=yob,
            phone=phone,
            gender=gender,
            height = height,
            address = address,
            description = description,
            image = image,
            measurements = measurements
        )
        new_service.save()

        return redirect(url_for('admin'))

@app.route('/edit/<id>', methods = ["GET", "POST"])
def edit(id):
    service = Service.objects.with_id(id)
    if request.method == "GET":
        return render_template('edit-service.html', service = service)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form ['yob']
        phone = form ['phone']
        if form['gender'] == 'Male':
            gender = 1
        else:
            gender = 0
        service = Service.update(
            set__name=name,
            set__yob=yob,
            set__phone=phone,
            set__gender=gender)
        return redirect(url_for('admin'))
    else:
        return "Not Found"


@app.route('/detail/<id>')
def detail(id):
    if 'loggedin' in session:
        if session['loggedin'] == True:
            service = Service.objects.with_id (id)
            return render_template('detail.html', service = service)
        else:
            return redirect(url_for('signin'))
    else:
        return redirect(url_for('signin'))

@app.route('/sign-in', methods = ["GET", "POST"])
def signin ():
    if request.method == "GET":
        return render_template('signin.html')
    elif request.method == "POST":
        form = request.form
        users = User.objects()
        username = form['username']
        password = form['password']
        logged = False

        for user in users:
            if username == user.username and password == user.password:
                logged = True
                session['id'] = str(user.id)

        if logged:
            session['loggedin'] = True
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('signin'))

@app.route('/sign-up', methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        form = request.form
        new_user = User(
            username = form['username'],
            password = form['password'],
            email = form['email'],
            fullname = form['fullname']
        )
        new_user.save()
        return redirect(url_for('signin'))

@app.route('/log-out')
def logout():
    session['loggedin'] = False
    return redirect(url_for('signin'))

@app.route('/order/<order_id>')
def order(order_id):
    new_order = Order(
        service_id = order_id,
        user_id = session['id'],
        time = str(datetime.now()),
        is_accepted = False
    )
    new_order.save()
    return "Đã gửi yêu cầu"

@app.route('/orderlist')
def orderlist():
    orders = Order.objects()
    return render_template('order.html', orders = orders)

@app.route('/update_order/<update_order_id>')
def update_order(update_order_id):
    order = Order.objects.with_id(update_order_id)
    order.update(set__is_accepted = True)
    return "Yêu cầu của bạn đã được xử lý"

if __name__ == '__main__':
  app.run(debug=True)
 