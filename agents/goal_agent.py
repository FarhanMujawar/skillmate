from utils.chains import simple_prompt_response

def goal_node(state, config=None):
    user_goal = state.input
    return {"goal": user_goal}
