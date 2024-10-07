from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Raj',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'oct-07-2024',
    },
    {
        'author': 'Raj',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'oct-07-2024',
    },
    {
        'author': 'Raj',
        'title' : 'Blog Post 3',
        'content' : 'Third Post Content',
        'date_posted' : 'oct-07-2024',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title='about')

if __name__ == "__main__":
    app.run(debug=True)