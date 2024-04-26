"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib, subprocess

root = pathlib.Path(__file__).parent.resolve()

epytc_version = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in epytc_version

# Get the long description from the README file
long_description = (root / "README.md").read_text(encoding="utf-8")

setup(
    name="epytc",
    version=epytc_version,
    description="An open-source Python package for modeling water quality in water distribution systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SWIL-IITK/EPyT-C",
    author="Gopinbathan R Abhijith",
    author_email="abhijith@iitk.ac.in",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    keywords="epanet, water, networks, quality, simulations, water quality modelling",
    python_requires=">=3.8",
    packages=find_packages(include=["epytc", "epytc.*"]),
    # include the defaul_values.yaml file
    package_data={"": ["*.yaml"]},
    install_requires=["epyt", "hydra-core"],
)
