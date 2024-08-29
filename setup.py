from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

    if HYPEN_E_DOT in requirements:     # to remove '-e .' from above requirements list
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = 'end2end', 
    version = '0.0.1',
    author = 'kabilan',
    author_email = 'kabilanp942@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)