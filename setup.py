import setuptools

with open("README.md", "r") as text:
    long_description = text.read()

setuptools.setup(
    name="pubmed-dl",
    version="0.1.0",
    author="",
    author_email="",
    description=("A simple Pubmed records download pipeline"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PathwayCommons/pubmed-dl".
    packages=setuptools.find_packages(),
    keywords=["",""],
    classifiers=[""],
    python_requires="",
    install_requires=[""],
    extras_require={},
)