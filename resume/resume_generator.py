from mithril import h
from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml

env = Environment(
    loader=FileSystemLoader('./templates')
)
def job_template(place):
    achievements = []
    if "achievements" in place:
        achievements = [h("li", achievement) for achievement in place["achievements"]]
    return h("div", {"class":"place"},
            h("h4", h("b", place["company"]), "|", place["role"]),
            h("h5", place["duration"], "|", place["location"]),
            h("ul", *achievements)
        )

def project_template(project):
    return h("label", {"class": "project", "for": project["id"]},
        h("h4", {"class": "name"}, project["name"]),
        h("ul", {"class": "tech"}, *[h("li", tech) for tech in project["tech"]]),
        h("p",  {"class", "description"}, project["description"])
    )

with open('resume.yml', 'r') as f:
    jobs = h("div", {"class" : "experience"},
            h("h3", "Work Experience"))
    doc = yaml.load(f)
    for job in doc:
        jobs.insert(job_template(job))
    template = env.get_template('index.html')
    with open('index.html', 'w') as f:
        f.write(template.render(jobs=jobs))
"""
with open('projects.yml', 'r') as f:
    projects = h("div", {"class": "description"})
    projects_section = h("section", {"id": "projects"},
                        h("h2", "Projects"),
                        projects)
    doc = yaml.load(f)
    for project in doc:
        #projects.insert(h("input", {"type": "checkbox", "id": project["id"], "name" : "project-select"}))
        projects.insert(project_template(project))
    
    with open("projects.html", "w") as of:
        of.write(str(projects_section))
"""
