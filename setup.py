from distutils.core import setup

setup(
    name="path_finder",
    packages=["path_finder"],
    version="0.1",
    license="MIT",
    description="interface for finding directories and files",
    author="Renier Kramer",
    author_email="renierkramer1987@gmail.com",
    url="https://github.com/hdsr-mid/path_finder",
    download_url="xx",
    keywords=["path", "directory", "regex", "find"],
    install_requires=["pathlib", "pytest", "typing"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
