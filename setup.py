from setuptools import setup, find_packages

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="climenus",  # Your new package name
    version="0.1.0",
    author="VencordThemer",
    author_email="vencordthemer@users.noreply.github.com",
    description="A simple framework for building interactive CLI menus in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vencordthemer/simplecli",
    project_urls={
        "Bug Tracker": "https://github.com/vencordthemer/simplecli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="cli, menu, terminal, console, interactive",
    packages=find_packages(),
    python_requires=">=3.6",
)

