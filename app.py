from flask import Flask, render_template, request
import os

from models.resume_parser import extract_text
from models.skills import extract_skills
from models.ats import calculate_ats_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["resume"]

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        resume_text = extract_text(filepath)

        skills = extract_skills(resume_text)

        ats_score = calculate_ats_score(skills)

        return render_template(
            "result.html",
            skills=skills,
            score=ats_score,
            text=resume_text
        )

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)