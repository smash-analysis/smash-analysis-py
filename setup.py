import os
from setuptools import setup

setup(name='smash-analysis',
      version='0.0.1',
      description='Analysis tool for processing SSB videos',
      license='MIT',
      author='John Moses, Jack Ceverha',
      py_modules=['smash-analysis'],
      url='https://github.com/smash-analysis/smash-analysis-py',
      include_package_data=True,
      packages=['numpy', 'cv2']
)
