from setuptools import setup, find_packages

setup(
    name="hapi",
    version="1.0",
    packages=find_packages(),

    install_requires=['numpy'],

    # metadata
    author="hitran.org",
    author_email="michael.aye@lasp.colorado.edu",
    description="Software for interfacing the HITRAN database",
    license="BSD 3-clause",
    keywords="HITRAN",
    url="http://hitran.org",
)
