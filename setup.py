import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'yaxil',
    'retry',
    'natsort',
    'pillow',
    'nibabel',
    'selfie',
    'executors',
    'vnav'
]

test_requirements = [
]

about = dict()
with open(os.path.join(here, 't2qc', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=find_packages(),
    package_data={
        '': ['*.tar.gz']
    },
    include_package_data=True,
    scripts=[
        'scripts/t2QC.py'
    ],
    install_requires=requires,
    tests_require=test_requirements
)
