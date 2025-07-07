from langchain.schema import RunnableConfig
from utils.chains import simple_prompt_response

def goal_node(state, config: RunnableConfig = None):
    user_goal = state["input"]
    return {"goal": user_goal}
