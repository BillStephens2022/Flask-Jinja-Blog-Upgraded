from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/ef76f82bb6da04f755f7").json()
print(posts)

@app.route("/")
def get_all_posts():
    print(posts)
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
