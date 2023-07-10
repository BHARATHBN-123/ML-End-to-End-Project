from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT  ='-e .'
def Get_Requirements(file_path:str)->List[str]:

    '''
    this function Returns a list of Requiements
    
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements =file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)





setup(name="ML PROJECT",
      version="0.0.1",
      author="BHARATH B N",
      packages=find_packages(),
      install_requires=Get_Requirements("requirements.txt"),)