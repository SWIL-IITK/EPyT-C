"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="epyt_c",
    version="0.0.1",
    description="An open-source Python package for modeling water quality in water distribution systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SWIL-IITK/EPyT-C",
    author="Gopinbathan R Abhijith",
    author_email="abhijith@iitk.ac.in",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",  # todo - specify the supported python versions
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="EPANET, EPyT, water quality modelling",
    packages=find_packages(include=['epyt_c', 'epyt_c.*']),
    python_requires=">=3.7, <4",
    install_requires=["epyt",
                      "numpy",
                      "pandas",
                      "xlsxwriter"],
    extras_require={  # Optional
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
)
