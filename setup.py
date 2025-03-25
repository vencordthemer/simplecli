from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simplecli",
    version="0.1.0",
    author="vencordthemer",
    description="A simple framework for building interactive CLI menus in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/interactivecli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
