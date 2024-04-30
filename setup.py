from setuptools import setup, find_packages

setup(
    name='nasa_apod',
    version='1.0.3',
    packages=find_packages(),
    install_requires=['requests'],
    author='Anjaneyulu Aerrolla',
    author_email='aaerrolla@gmail.com',
    description='Python package for interacting with NASA APO API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aaerrolla/nasa_apod',
    license='MIT',
)