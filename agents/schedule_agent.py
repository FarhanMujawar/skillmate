from utils.chains import simple_prompt_response

def schedule_node(state, config=None):
    skills = state["skills"]
    prompt = f"Create a 4-week study plan to master these skills:\n{skills}"
    schedule = simple_prompt_response(prompt)
    return {"schedule": schedule}
