from langgraph.graph import StateGraph, END
from pydantic import BaseModel
from agents.goal_agent import goal_node
from agents.skill_agent import skill_node
from agents.resource_agent import resource_node
from agents.schedule_agent import schedule_node
from agents.quiz_agent import quiz_node
from agents.resume_agent import resume_node

class StateSchema(BaseModel):
    input: str
    goal: str = ""
    skills: str = ""
    resources: str = ""
    schedule: str = ""
    quiz: str = ""
    resume: str = ""

def build_graph():
    graph = StateGraph(StateSchema)
    
    graph.add_node("Goal", goal_node)
    graph.add_node("Skills", skill_node)
    graph.add_node("Resources", resource_node)
    graph.add_node("Schedule", schedule_node)
    graph.add_node("Quiz", quiz_node)
    graph.add_node("Resume", resume_node)

    graph.set_entry_point("Goal")
    
    graph.add_edge("Goal", "Skills")
    graph.add_edge("Skills", "Resources")
    graph.add_edge("Resources", "Schedule")
    graph.add_edge("Schedule", "Quiz")
    graph.add_edge("Quiz", "Resume")
    graph.add_edge("Resume", END)

    return graph.compile()
