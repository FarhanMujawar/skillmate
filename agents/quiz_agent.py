from utils.chains import simple_prompt_response

def quiz_node(state, config=None):
    skills = state["skills"]
    prompt = f"Generate 3 simple quiz questions with answers based on these skills:\n{skills}"
    quiz = simple_prompt_response(prompt)
    return {"quiz": quiz}
