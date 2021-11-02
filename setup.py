from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="pyresolve",
    version="1.1.0",
    author="fiverr",
    author_email="devops@fiverr.com",
    description="Resolve dot notation from dictionary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fiverr/pyresolve",
    license="MIT",
    packages=['pyresolve'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2',
)
