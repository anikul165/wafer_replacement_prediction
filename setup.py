from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='The goal is to build a machine learning model that predicts whether a semiconductor wafer needs to be replaced based on readings from various sensors. The model performs binary classification, predicting whether the wafer is working or needs replacement, represented by classes +1 and -1.',
    author='anikul165',
    license='MIT',
)
