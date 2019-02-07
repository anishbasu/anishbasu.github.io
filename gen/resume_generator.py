from mithril import h
import yaml

def job_template(place):
    achievements = []
    if "achievements" in place:
        achievements = [h("li", achievement) for achievement in place["achievements"]]
    return h("label", {"class":"place"},
        h("div", {"class": "heading"},
            h("h4", {"class":"role"}, place["role"]),
            h("h5", {"class":"company"}, place["name"])
        ),
        h("h5", {"class":"duration"},place["duration"]),
        h("summary", place["summary"].strip()),
        h("ul",
            *achievements
        )
    )

def project_template(project):
    return h("label", {"class": "project", "for": project["id"]},
        h("h4", {"class": "name"}, project["name"]),
        h("ul", {"class": "tech"}, *[h("li", tech) for tech in project["tech"]]),
        h("p",  {"class", "description"}, project["description"])
    )

with open('resume.yml', 'r') as f:
    jobs = h("div", {"class": "description"})
    job_section = h("section", {"id": "work"},
                        h("h2", "Work"),
                        jobs)
    doc = yaml.load(f)
    for job in doc:
        #jobs.insert(h("input", {"type": "checkbox", "id": job["place"]["id"], "name" : "work-select"}))
        jobs.insert(job_template(job["place"]))
    with open("jobs.html", "w") as of:
        of.write(str(job_section))

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
