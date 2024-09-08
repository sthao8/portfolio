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
         "description": "Bank app built with Bootstrap, Flask, with seeded customers in customizable locales supported by Faker stored in a relational MySQL database.",
         "url": "https://bank-sthao8.pythonanywhere.com",
         "source_code": "https://github.com/sthao8/bank"
         },
        {"name": "Hotel Booking System",
         "description": "Hotel booking system built with Bootstrap, Flask in Python with data stored in MySQL relational databases.",
         "url": None,
         "source_code": "https://github.com/sthao8/BluePrintsHotel"
         },
         {"name": "Plant Journal",
         "description": "My first project made with Flask written in Python! A cute plant journal with data stored in SQLite databases, feature plant search via API lookup!",
         "url": None, #"https://plantjournal-sthao8.pythonanywhere.com",
         "source_code": "https://github.com/sthao8/plant_journal"
         },
         {"name": "Portfolio",
         "description": "A responsive portfolio coded by Shoua Thao with Flask and styled by Bootstrap.",
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
            "url": "/static/Shoua_Thao_CV_ENG.pdf",
            "icon": "bxs-file",
            "title": "CV"
        }
    ]

    about_me_text = "Energized by finding solutions to problems, solving puzzles, and lifelong learning, I make carefully crafted and responsive apps with an eye for design."
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

