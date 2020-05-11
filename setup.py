from setuptools import setup

setup(
     name='py-scripto',
     version='0.1.0',
     author='datnguye',
     author_email='datnguyen.it09@gmail.com',
     packages=['py-scripto'],
     scripts=['bin/py-scripto'],
     url='https://github.com/datnguye/py-scripto',
     license='LICENSE',
     description='A package to run SQL script or SQL file script in an instance of sql server',
     long_description=open('README.md').read(),
     install_requires=["pyodbc==4.0.30"],
)