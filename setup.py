import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pubmed-dl",
    version="0.1.0",
    author="Anweshi Anavadya",
    author_email="anweshianavadya@gmail.com",
    description=("A simple Pubmed records download pipeline."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PathwayCommons/pubmed-dl",
    packages=setuptools.find_packages(),
    keywords=["pubmed", "eutils", "pubmed-download", "pathwaycommons"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
    ],
    entry_points={
        "console_scripts": ["pubmed-dl=pubmed_dl.main:main"],
    },
    python_requires=">=3.8.0",
    install_requires=[
        "biopython>=1.78",
        "requests>=2.25.1",
        "pydantic>=1.7.3",
        "python-dotenv>=0.15.0",
        "typer>=0.3.2",
    ],
    extras_require={
        "dev": ["black", "coverage", "codecov", "flake8", "pytest", "pytest-cov", "mypy"]
    },
)
