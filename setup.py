"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['epyt','pandas', 'xlswriter','numpy']

test_requirements = [ ]

setup(
    author="Gopinathan R Abhijith",
    author_email='abhijith@iitk.ac.in',
    python_requires='>=3.8, <=3.11',
    classifiers=[
        'Development Status :: 1',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.11',
            ],
    description="A python package for modeling water quality in water distribution systems.",
    install_requires=requirements,
    license="Open source license",
    include_package_data=True,
    keywords='epyt_c',
    name='epyt_c',
    packages=find_packages(include=['epyt_c', 'epyt_c.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tylertrimble/viswaternet',
    version='1.2.0',
    zip_safe=False,
)
