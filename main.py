import matplotlib.pyplot as plt
import json


def load_user_data(filename):
    file = open(filename)
    data = json.load(file)
    file.close()
    return data


def main():
    # Set attributes
    data = load_user_data("personA.json")
    Header = ">>>This resume was generated entirely in Python."
    Name = data["name"]
    Title = data["title"]
    Contact = data["address"] + "\n" + data["mobilePhone"] + "\n" + data["email"] + "\n" + data["website"]
    ProjectsHeader = "PROJECTS"
    ProjectOneTitle = "Project One Name"
    ProjectOneDesc = "- Description 1\n- Another description 2\n- Yeah I carried my team of 5 to success"
    ProjectTwoTitle = "Project Two name"
    ProjectTwoDesc = (
        "- Description 1 with some example\n- Able to push the team to finish it 5 days earlier than deadline"
    )
    WorkHeader = "EXPERIENCE"
    WorkOneTitle = data["experiences"][0]["company"] + " / " + data["experiences"][0]["position"]
    WorkOneTime = data["experiences"][0]["period"]
    WorkOneDesc = "- " + data["experiences"][0]["description"][0] + "\n- " + data["experiences"][0]["description"][1]
    WorkTwoTitle = data["experiences"][1]["company"] + " / " + data["experiences"][1]["position"]
    WorkTwoTime = data["experiences"][1]["period"]
    WorkTwoDesc = (
        "- "
        + data["experiences"][1]["description"][0]
        + "\n- "
        + data["experiences"][1]["description"][1]
        + "\n- "
        + data["experiences"][1]["description"][2]
    )
    EduHeader = "EDUCATION"
    EduOneTitle = "Example University, Bachelor of Business Administration"
    EduOneTitle = data["educations"][0]["university"] + ", " + data["educations"][0]["degree"]
    EduOneTime = data["educations"][0]["period"]
    EduTwoTitle = data["educations"][1]["university"] + ", " + data["educations"][1]["degree"]
    EduTwoTime = data["educations"][1]["period"]
    SkillsHeader = "Skills"
    SkillsDesc = "- Python\n- Panas\n- NumPy\n- Data Visualization\n- Data Cleaning\n- Command Line\n- Git and Version Control\n- SQL\n- APIs\n- Probability/Statistics\n- Data Manipulation\n- Excel"
    ExtrasDesc = "Learned popular data science\nlanguages, data cleaning and\nmanipulation, machine learning \nand statistical analysis"

    # set font
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = "STIXGeneral"

    fig, ax = plt.subplots(figsize=(8.5, 11))

    # Decorative Lines
    ax.axvline(x=0.5, ymin=0, ymax=1, color="#007ACC", alpha=0.0, linewidth=50)
    plt.axvline(x=0.99, color="#000000", alpha=0.5, linewidth=300)
    plt.axhline(y=0.88, xmin=0, xmax=1, color="#ffffff", linewidth=3)

    # set background color
    ax.set_facecolor("white")

    # remove axes
    plt.axis("off")

    # add text
    plt.annotate(Header, (0.02, 0.98), weight="regular", fontsize=8, alpha=0.6)
    plt.annotate(Name, (0.02, 0.94), weight="bold", fontsize=20)
    plt.annotate(Title, (0.02, 0.91), weight="regular", fontsize=14)
    plt.annotate(Contact, (0.7, 0.906), weight="regular", fontsize=8, color="#ffffff")

    plt.annotate(ProjectsHeader, (0.02, 0.86), weight="bold", fontsize=10, color="#58C1B2")
    plt.annotate(ProjectOneTitle, (0.02, 0.832), weight="bold", fontsize=10)
    plt.annotate(ProjectOneDesc, (0.04, 0.78), weight="regular", fontsize=9)
    plt.annotate(ProjectTwoTitle, (0.02, 0.745), weight="bold", fontsize=10)
    plt.annotate(ProjectTwoDesc, (0.04, 0.71), weight="regular", fontsize=9)

    plt.annotate(WorkHeader, (0.02, 0.54), weight="bold", fontsize=10, color="#58C1B2")
    plt.annotate(WorkOneTitle, (0.02, 0.508), weight="bold", fontsize=10)
    plt.annotate(WorkOneTime, (0.02, 0.493), weight="regular", fontsize=9, alpha=0.6)
    plt.annotate(WorkOneDesc, (0.04, 0.445), weight="regular", fontsize=9)
    plt.annotate(WorkTwoTitle, (0.02, 0.4), weight="bold", fontsize=10)
    plt.annotate(WorkTwoTime, (0.02, 0.385), weight="regular", fontsize=9, alpha=0.6)
    plt.annotate(WorkTwoDesc, (0.04, 0.337), weight="regular", fontsize=9)

    plt.annotate(EduHeader, (0.02, 0.185), weight="bold", fontsize=10, color="#58C1B2")
    plt.annotate(EduOneTitle, (0.02, 0.155), weight="bold", fontsize=10)
    plt.annotate(EduOneTime, (0.02, 0.14), weight="regular", fontsize=9, alpha=0.6)
    plt.annotate(EduTwoTitle, (0.02, 0.08), weight="bold", fontsize=10)
    plt.annotate(EduTwoTime, (0.02, 0.065), weight="regular", fontsize=9, alpha=0.6)
    
    plt.annotate(SkillsHeader, (0.7, 0.8), weight="bold", fontsize=10, color="#ffffff")
    plt.annotate(SkillsDesc, (0.7, 0.56), weight="regular", fontsize=10, color="#ffffff")
    plt.annotate(ExtrasDesc, (0.7, 0.345), weight="regular", fontsize=10, color="#ffffff")

    plt.savefig("resumeexample.pdf", dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
