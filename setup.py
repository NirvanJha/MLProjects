from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    :param file_path: str - path to the requirements file
    :return: List[str] - list of package names
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    
    # Remove any comments or empty lines
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    
    return requirements

setup(
    name='MLProject',
    version='0.1',
    author='Nirvan Jha',
    description='A machine learning project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author_email='nirvanjha30@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

