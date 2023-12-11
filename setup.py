from os import path
from setuptools import find_packages
from setuptools import setup


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

version = "1.7"

install_requires = []
tests_require = [
    "pytest",
]

setup(
    name="path_finder",
    packages=find_packages(include=["path_finder", "path_finder.*"]),
    version=version,
    license="MIT",
    description="An interface for finding directories and files",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Renier Kramer",
    author_email="renier.kramer@hdsr.nl",
    url="https://github.com/hdsr-mid/path_finder",
    download_url=f"https://github.com/hdsr-mid/path_finder/archive/v{version}.tar.gz",
    keywords=["interface", "path", "directory", "filename", "glob", "regex", "find"],
    zip_safe=False,
    python_requires=">3.7",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
