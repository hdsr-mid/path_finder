from distutils.core import setup


version = "0.2"

long_description = "\n\n".join([open("README.md").read()])

install_requires = [
    "pathlib",
    "typing",
]

tests_require = [
    "pytest",
]

setup(
    name="path_finder",
    packages=["path_finder"],
    version=version,
    license="MIT",
    description="interface for finding directories and files",
    long_description=long_description,
    author="Renier Kramer",
    author_email="renier.kramer@hdsr.nl",
    url="https://github.com/hdsr-mid/path_finder",
    download_url="https://github.com/hdsr-mid/path_finder/archive/v0.2.tar.gz",
    keywords=["interface", "path", "directory", "filename", "glob", "regex", "find"],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
