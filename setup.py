from setuptools import setup, find_packages

setup(
    name="aoc_utils",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
