import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="funcopy",
    version="0.2.0",
    description="funcopy: copy a func",
    long_description=README,
    long_description_content_type="text/markdown",
    author="TvoozMagnificent",
    author_email="luchang1106@icloud.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["funcopy"],
    include_package_data=True,
    install_requires=[],
)


