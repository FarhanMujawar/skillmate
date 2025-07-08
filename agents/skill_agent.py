from utils.chains import simple_prompt_response

def skill_node(state, config=None):
    goal = state.goal
    prompt = f"What are the top 5–7 skills needed for: {goal}?"
    skills = simple_prompt_response(prompt)
    return {"skills": skills}
