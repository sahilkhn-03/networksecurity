from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """This Fuction Will Return List Of Requirements ."""

    req_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file :
            lines = file.readlines()
            for line in lines:
                requirement =line.strip()
                if requirement and requirement != '-e .':
                    req_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found ")
    return req_lst
setup(
    name="networksecurity",
    version="0.0.1",
    author="Sahil",
    author_email = "sahilkhankhk5881@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
    )