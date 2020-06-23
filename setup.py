from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="pyresolve",
    version="0.0.1",
    author="omrilotan",
    author_email="omri@hamadgera.com",
    description="Resolve dot notation from dictionary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omrilotan/pyresolve",
    license="MIT",
    packages=['pyresolve'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
