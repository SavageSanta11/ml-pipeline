from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="ml-pipeline",
    version='0.0.1',
    author="SavageSanta11",
    author_email="codetechie11@gmail.com",
    packages=find_packages(), # will try to build src like a package since it as __init__.py 
    install_requires=get_requirements('requirements.txt')
)