from utils.chains import simple_prompt_response

def resource_node(state, config=None):
    skills = state.skills
    prompt = f"Suggest one good free learning resource for each of the following skills:\n{skills}"
    resources = simple_prompt_response(prompt)
    return {"resources": resources}
