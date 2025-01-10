import os
from pathlib import Path
import logging

logging.basicConfig(level =logging.INFO, format ='[%(asctime)s]:%(message)s:') #Time and execution name

project_name = "ML_Project"

# List of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", 
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

# Iterate through the list of files
for filepath in list_of_files:
    path = Path(filepath)
    # Create parent directories if they don't exist
    if path.parent != Path():
        path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {path.parent} for the file: {path.name}")
    
    # Create the file if it doesn't exist or is empty
    if not path.exists() or path.stat().st_size == 0:
        path.touch()
        logging.info(f"Creating empty file: {path}")
    else:
        logging.info(f"{path.name} already exists")