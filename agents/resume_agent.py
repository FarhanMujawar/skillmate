from jinja2 import Environment, FileSystemLoader

def resume_node(state, config=None):
    goal = state["goal"]
    skills = state["skills"].split('\n')
    schedule = state["schedule"]

    env = Environment(loader=FileSystemLoader("tools"))
    template = env.get_template("resume_template.jinja2")
    resume = template.render(goal=goal, skills=skills, schedule=schedule)
    
    return {"resume": resume}
