from setuptools import setup
from setuptools import find_packages

setup(name='Initial_setup',
      version='1.0',
      description='Basic Package Setup for New Conda Envirnment',
      author='Dong-Gyu Lee',
      author_email='kbo2010@gmail.com',
      url='https://github.com/dglee',
      download_url='https://github.com/dglee/Initial_setup',
      license='MIT',
      install_requires=['numpy>=1.15.4',
                        'scipy>=1.1.0',
                        'os',
                        'glob',
                        'datetime',
                        'opencv'
                        'matplotlib'
                        'scikit-learn'
                        'pandas'
                        ],
      package_data={'Setup': ['README.md']},
      packages=find_packages())
