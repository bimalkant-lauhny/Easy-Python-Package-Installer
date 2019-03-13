import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy-ppi",
    version="0.0.1",
    author="Bimalkant Lauhny, Mukesh Kharita",
    author_email="lauhny.bimalk@gmail.com",
    description="Easy Interpreter for managing pip packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/code-master5/Advanced-Python-Package-Installer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Ubuntu 18.04",
    ],
)
