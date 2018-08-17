from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
        "title" : "Thơ con c**",
        "content": "Một con vịt xòe ra hai cái cánh",
        "author" : "Khuyết danh",
        "author_sex" : 1
        },
        {
        "title" : "Thơ con c**",
        "content": "Hai con vịt xòe ra hai cái cánh",
        "author" : "Khuyết danh",
        "author_sex" : 1
        },
        {
        "title" : "Thơ con c**",
        "content": "Ba con vịt xòe ra hai cái cánh",
        "author" : "Khuyết danh",
        "author_sex" : 0
        },
        {
        "title" : "Thơ con c**",
        "content": "Bốn con vịt xòe ra hai cái cánh",
        "author" : "Khuyết danh",
        "author_sex" : 0
        },
        {
        "title" : "Thơ con c**",
        "content": "Năm con vịt xòe ra hai cái cánh",
        "author" : "Khuyết danh",
        "author_sex" : 1
        }
    ]
    
    # post = {
    #     "title" : "Thơ con c**",
    #     "content": "Một con vịt xòe ra hai cái cánh",
    #     "author" : "Khuyết danh"
    # }
    #mix data and template
    return render_template('index.html', posts = posts)
#kiểm tra xem file app có được chạy trực tiếp không
#chạy trực tiếp vs chạy gián tiếp

@app.route('/hello')
def say_hello():
    return 'Hello from the other side'

@app.route('/hi/<name>/<age>')
def say_hi(name, age):
    return "Hi {}, you're {} years old.".format (name, age)

@app.route('/sum/<int:x>/<int:y>')
def sum(x, y):
    # result = int(x) + int (y)
    return str(x +y)
if __name__ == '__main__':
  app.run(debug=True)
  #debug = true: cập nhật thay đổi mới nhất của server