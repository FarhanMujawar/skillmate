#for installing local package in my virtual environment

from setuptools import find_packages,setup

setup(
    name='skillmate',
    version='0.0.1',
    author='Farhan Mujawar',
    author_email='farhanmujawar0711@gmail.com',
    install_requires=["openai","langchain","huggingface_hub","streamlit","python-dotenv","sentence-transformers","langgraph","jinja2","tavily-python"],
    packages=find_packages()
)