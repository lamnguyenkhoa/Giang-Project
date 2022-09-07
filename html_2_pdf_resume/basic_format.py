import json
import os
import dominate
from dominate.tags import *

CSS_FILE = "basic_style.css"


def build_resume(resume_data):
    try:
        with open(CSS_FILE, "r") as f:
            css = f.read()
    except FileNotFoundError:
        css = ""

    doc = dominate.document(title="Resume")
    with doc.head:
        style(dominate.util.raw(css))
        script(type="text/javascript", src="script.js")

    with doc.add(div(id="resume")):
        h1(resume_data["name"])
        ul(
            li(resume_data["email"]),
            li(resume_data["mobilePhone"]),
            li(resume_data["website"]),
            li(resume_data["address"]),
        )
        p(resume_data["biography"])

        if len(resume_data["experiences"]) > 0:
            h2("Experience")
            for experience in resume_data["experiences"]:
                h3(
                    span(experience["position"] + ",   " + experience["company"]),
                    span(experience["period"]),
                )
                ul([li(highlight) for highlight in experience["description"]])

        if len(resume_data["projects"]) > 0:
            h2("Projects")
            for project in resume_data["projects"]:
                ...

        if len(resume_data["educations"]) > 0:
            h2("Education")
            for education in resume_data["educations"]:
                h3(
                    span(education["university"] + ",   " + education["degree"]),
                    span(education["period"]),
                )

        if len(resume_data["skills"]) > 0:
            h2("Skills")
            ul([li(skill) for skill in resume_data["skills"]])

    return doc


if __name__ == "__main__":
    with open("resume_data.json", "r") as file:
        resume_json = json.load(file)
    html = build_resume(resume_json)
    print(html.render())
