from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Application name:
    name="dcat-catalog-downloader",

    # Version number (initial):
    version="0.1.0",

    description='''Downloads DCAT RDF data from a DCAT catalog endpoint and merges it to query it locally''',
    long_description=long_description,

    # Application author details:
    author="Knud Möller",
    author_email="knud.moeller@berlinonline.de",

    # What does your project relate to?
    keywords='''DCAT tool RDF SPARQL open_data''',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(include=['berlinonline', 'berlinonline*']),

    scripts=['bin/download_catalog'],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/berlinonline/dcat-catalog-downloader",

    license="MIT License",

    # Dependent packages (distributions)
    install_requires=[
        "rdflib",
        "argparse"
    ],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],

)
