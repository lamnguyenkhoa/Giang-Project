import json
import os
import dominate
from dominate.tags import *

CSS_FILE = "two_column_style.css"


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

    with doc.add(div(id="resume-left")):
        p(resume_data["biography"], id="biography")

        ul(
            li(resume_data["email"]),
            li(resume_data["mobilePhone"]),
            li(resume_data["website"]),
            li(resume_data["address"]),
        )

        if len(resume_data["skills"]) > 0:
            h2("Skills")
            ul([li(skill) for skill in resume_data["skills"]])

        if len(resume_data["awards"]) > 0:
            h2("Awards")
            for award in resume_data["awards"]:
                tmp = "{name} ({period})".format(name=award["name"], period=award["period"])
                p(tmp)

    with doc.add(div(id="resume-right")):
        h1(resume_data["name"])
        h2(resume_data["title"], id="job-title")

        if len(resume_data["experiences"]) > 0:
            h2("Experiences")
            for experience in resume_data["experiences"]:
                h3(
                    span(experience["position"] + ",   " + experience["company"]),
                    span(experience["period"]),
                )
                ul([li(highlight) for highlight in experience["description"]])

        if len(resume_data["projects"]) > 0:
            h2("Projects")
            for project in resume_data["projects"]:
                h3(
                    span(project["name"] + ",   " + project["position"]),
                    span(project["period"]),
                )
                ul(
                    li(project["description"]),
                    li(project["technology"]),
                )

        if len(resume_data["educations"]) > 0:
            h2("Education")
            for education in resume_data["educations"]:
                p(education["degree"])
                ul(
                    li(education["university"] + " | " + education["period"]),
                )
    return doc


if __name__ == "__main__":
    with open("resume_data.json", "r") as file:
        resume_json = json.load(file)
    html = build_resume(resume_json)
    print(html.render())
