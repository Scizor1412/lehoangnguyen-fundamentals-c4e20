from flask import Flask, render_template,redirect
app = Flask(__name__)


@app.route('/')
def index():
    return "Go to /about-me or /school"

@app.route('/about-me')
def about_me():
    about_me = {
    "Name" : "Scizor",
    "Work" : "Editor",
    "School" : "Techkids-Coding Schools",
    "Hobbies" : "League of Legends, football, films, Pokemon",
    "Favourite_films" : "The Vow, 100 days of Summer, Shawshank Redemption, Inception, Grown up",
    "Crush": "Error: 404 Not Found",
    "Gf" : "Not Exist",
    }
    return render_template('about_me.html', about_me=about_me)

@app.route('/school')
def school():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)