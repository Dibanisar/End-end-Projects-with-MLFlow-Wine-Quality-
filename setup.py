from setuptools import setup, find_packages

# Read the contents of your README file to use it as the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="End-end-Projects-with-MLFlow",
    version="0.0.0",
    author="Dibanisa Fakude",
    author_email="dibanisaf@gmail.com",
    description="A python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dibanisar/End-end-Projects-with-MLFlow",
    packages=find_packages(where="src"),  # This ensures packages are found in src
    package_dir={"": "src"},  # Points to the src directory for packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pandas",
        "mlflow==2.2.2",
        "notebook",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "python-box==6.0.2",
        "pyYAML",
        "tqdm",
        "ensure",
        "joblib",
        "types-PyYAML",
        "Flask",
        "Flask-Cors",
    ],
    python_requires=">=3.6"
)
