import os
os.environ.pop("SSL_CERT_FILE", None)
import streamlit as st
from graph.langgraph_config import build_graph

st.title("🎓 SkillMate 2.0 – Advanced AI Skill Coach")

goal_input = st.text_input("Enter your career goal")

if goal_input and st.button("Start Coaching"):
    try:
        with st.spinner("Running AI agents..."):
            graph = build_graph()
            result = graph.invoke({"input": goal_input})

        st.subheader("🎯 Goal")
        st.write(result["goal"])

        st.subheader("🧠 Skills Required")
        st.write(result["skills"])

        st.subheader("📚 Learning Resources")
        st.write(result["resources"])

        st.subheader("📅 Schedule")
        st.write(result["schedule"])

        st.subheader("🧪 Quiz")
        st.write(result["quiz"])

        st.subheader("📄 Resume")
        st.code(result["resume"])
    except Exception as e:
        st.error(f"An error occurred: {e}")
