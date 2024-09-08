from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    image="/static/lotus.jpg"
    projects = [
        {"name": "Bank App",
         "description": "stuff",
         "url": "https://bank-sthao8.pythonanywhere.com"},
        {"name": "Hotel Booking System",
         "description": "more stuff",
         "url": "#"},
         {"name": "Plant Journal",
         "description": "plant journal description",
         "url": "https://plantjournal-sthao8.pythonanywhere.com"},
         {"name": "Portfolio",
         "description": "You're visiting this page, silly!",
         "url": "#"}
    ]
    about_me_text = "Hello, world! I'm a student at Teknikhögskolan studying Python with a focus in AI looking for a LIA-internship for weeks 40-47."
    email = "shoua.thao@studerande.plushogskolan.se"
    
    return render_template(
        "index.html",
        image=image,
        projects=projects,
        about_me_text=about_me_text,
        email=email)

if __name__ == "__main__":
    app.run(debug=True)

