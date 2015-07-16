from setuptools import setup, find_packages

setup(
    name="hapi",
    version="1.0",
    packages=find_packages(),

    install_requires=['numpy'],

    # metadata
    author="hitran.org",
    # I am not the author of the physcis code in this package.
    # I'm only the packager. And added a notebook or two.
    author_email="michael.aye@lasp.colorado.edu",
    # author email just set to mine to avoid HITRAN team to be bothered by questions
    # about this package. 
    description="Software for interfacing the HITRAN database",
    license="BSD 3-clause",
    keywords="HITRAN",
    url="http://hitran.org",
)
