from setuptools import setup
from setuptools import find_packages

setup(
    name="bs",
    description="No-bullshit base conversion.",
    version="1.0.0",
    url="https://github.com/Kevinpgalligan/bs",
    author="Kevin Galligan",
    author_email="galligankevinp@gmail.com",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    install_requires=[]
)
