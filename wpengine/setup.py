from setuptools import setup

setup(
    name = "task",
    version = "0.0.1",
    author = "",
    author_email = "",
    description = ("Python project for wpengine  evaluation"),
    license = "BSD",
    packages=['task', 'tests','data'],
    data_files=[('.',['data','main.py'])],
    include_package_data=True
    )
