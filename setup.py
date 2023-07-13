import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPONAME = "CNN-Classifier"
AUTHOR_USER_NAME = "yashguptatech"
SRC_REPO = "CNN-Classifier"
AUTHOR_EMAIL = "yashgupta.tech@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
        
)