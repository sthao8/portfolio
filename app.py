from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    image = "/static/image.jpg"
    skills = [
        {
            "name": "Python",
            "icon": "bxl-python"
        },
        {
            "name": "HTML",
            "icon": "bxl-html5"
        },
        {
            "name": "CSS",
            "icon": "bxl-css3"
        },
        {
            "name": "Javascript",
            "icon": "bxl-javascript"
        },
        {
            "name": "MySQL",
            "icon": "bxs-data"
        },
        {
            "name": "Flask",
            "icon": "bxl-flask"
        },
        {
            "name": "AI/ML",
            "icon": "bx-math"
        },
        {
            "name": "Bootstrap",
            "icon": "bxl-bootstrap"
        },
        {
            "name": "C",
            "icon": "bx-code-curly"
        }
    ]
    projects = [
        {"name": "Bank App",
         "description": "A full-featured bank app with a cool seeding function for faking locale-specific data stored in a MySQL database. Has ability to (advanced) search, sort, and paginate customers, as well as loading more account transactions via AJAX for the ultimate no-reload experience.",
         "url": "https://bank-sthao8.pythonanywhere.com",
         "source_code": "https://github.com/sthao8/bank"
         },
        {"name": "Hotel Booking System",
         "description": "Hotel booking and management system - an exercise in CRUD operations using MySQL for data management. Also looks really good!",
         "url": None,
         "source_code": "https://github.com/sthao8/BluePrintsHotel"
         },
         {"name": "Plant Journal",
         "description": "My first web app! A cute plant journal featuring emojis for icons (!) and plant search via third-party API calls. Learned a lot about integrating external APIs and handling user-input data with SQLite. Manual implementations of pagination, user management, and form validation.",
         "url": "https://plantjournal-sthao8.pythonanywhere.com",
         "source_code": "https://github.com/sthao8/plant_journal"
         },
         {"name": "Portfolio",
         "description": "An elegant and beautifully responsive portfolio, coded and designed by me using Flask and made pretty with Bootstrap. You're demoing it live right now!",
         "url": None,
         "source_code": "https://github.com/sthao8/portfolio"
         }
    ]

    links = [
        {
            "url": "https://www.linkedin.com/in/shoua-thao-7986512bb/",
            "icon": "bxl-linkedin",
            "title": "LinkedIn"
        },
        {
            "url": "https://github.com/sthao8",
            "icon": "bxl-github",
            "title": "Github"
        },
        {
            "url": "https://www.instagram.com/shoouey/",
            "icon": "bxl-instagram-alt",
            "title": "Instagram"
        },
        {
            "url": "/static/Shoua_Thao_CV_ENG.pdf",
            "icon": "bxs-file",
            "title": "CV"
        }
    ]

    about_me_text = "Energized by finding solutions to problems, learning, and learning by finding solutions to problems, I make carefully crafted back- and frontend with an eye for design and a special interest in data analysis via AI/ML. I do digital art in my free time!"
    email = "shoua.thao@studerande.plushogskolan.se"
    
    return render_template(
        "index.html",
        image=image,
        projects=projects,
        about_me_text=about_me_text,
        email=email,
        skills=skills,
        links=links)

if __name__ == "__main__":
    app.run(debug=True)

