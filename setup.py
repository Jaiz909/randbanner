from setuptools import setup

setup(name='randbanner',
      version='1.0',
      description='Random banner generator with colour support.',
      author='Jai Grimshaw',
      author_email='randbanner@jaigrimshaw.com',
      license='MIT',
      install_requires=[
          'clint',
          'pyfiglet',
      ],
      scripts=['bin/randbanner'])