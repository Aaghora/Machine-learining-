from setuptools import setup, find_packages
from typing import List

#Declearing variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Kirandev"
DESCRIPTION="This is House predictor"

REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_lists()->List[str]:
    """
    This function is going to return list of all the requirements 
    mentioned in requirements.txt file  

    return This function is going to return a list which contains 
    name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name= PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_lists()


)