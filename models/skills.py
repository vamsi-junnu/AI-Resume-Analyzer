import re

# Add more skills as needed
SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "flask",
    "django",
    "sql",
    "mysql",
    "mongodb",
    "git",
    "github",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pandas",
    "numpy",
    "opencv",
    "aws",
    "docker",
    "linux"
]


def extract_skills(text):
    text = text.lower()

    found = []

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.append(skill)

    return sorted(list(set(found)))