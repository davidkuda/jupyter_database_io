from distutils.core import setup
from setuptools import find_packages

setup(
    name="db_connector",
    version="0.1",
    description="Config mgt to connect to dbs.",
    author="David Kuda",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
