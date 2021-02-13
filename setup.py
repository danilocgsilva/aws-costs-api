from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="aws_costs_api",
    version=VERSION,
    description="Api to checks and analises the aws costs",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="AWS costs api",
    url="https://github.com/danilocgsilva/aws-costs-api",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["aws_costs_api"],
    include_package_data=True
)
