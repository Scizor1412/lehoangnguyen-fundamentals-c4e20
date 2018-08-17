from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "go to /user/<username> to get user's information"

@app.route('/user/<username>')
def users(username):
    users = [
        {
            "Name" : "Scizor",
            "Work" : "Editor",
            "School" : "Techkids-Coding Schools",
            "Hobbies" : "League of Legends, football, films, Pokemon",
            "Favourite_films" : "The Vow, 100 days of Summer, Shawshank Redemption, Inception, Grown up",
            "Crush": "Error: 404 Not Found",
            "Gf" : "Not Exist"
        },
        {
            "Name" : "Leafeon",
            "Work" : "Editor",
            "School" : "Techkids-Coding Schools",
            "Hobbies" : "League of Legends, football, films, Pokemon",
            "Favourite_films" : "The Vow, 100 days of Summer, Shawshank Redemption, Inception, Grown up",
            "Crush": "Error: 404 Not Found",
            "Gf" : "Not Exist"
        },
        {
            "Name" : "Vaporeon",
            "Work" : "Editor",
            "School" : "Techkids-Coding Schools",
            "Hobbies" : "League of Legends, football, films, Pokemon",
            "Favourite_films" : "The Vow, 100 days of Summer, Shawshank Redemption, Inception, Grown up",
            "Crush": "Error: 404 Not Found",
            "Gf" : "Not Exist"
        },
        {
            "Name" : "Jolteon",
            "Work" : "Editor",
            "School" : "Techkids-Coding Schools",
            "Hobbies" : "League of Legends, football, films, Pokemon",
            "Favourite_films" : "The Vow, 100 days of Summer, Shawshank Redemption, Inception, Grown up",
            "Crush": "Error: 404 Not Found",
            "Gf" : "Not Exist"
        },
        {
            "Name" : "Pikachu",
            "Work" : "Editor",
            "School" : "Techkids-Coding Schools",
            "Hobbies" : "League of Legends, football, films, Pokemon",
            "Favourite_films" : "The Vow, 100 days of Summer, Shawshank Redemption, Inception, Grown up",
            "Crush": "Error: 404 Not Found",
            "Gf" : "Not Exist"
        }
    ]
    run = False
    for index, user in enumerate(users):
        if username == user["Name"]:
            n = index
            run = True
    if run:
        return render_template ('Users.html', user = users[n])
    else:
        return "User not found"

if __name__ == '__main__':
  app.run(debug=True)