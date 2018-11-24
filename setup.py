from os import path
from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements(path.join(path.dirname(__file__), 'requirements.txt'), session='')
reqs = [str(ir.req) for ir in install_reqs]
test_reqs = ['pytest']

setup(
    name='dobbie',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'dobbie = dobbie.__main__:main',
        ]
    },
    install_requires=reqs,
    tests_require=test_reqs,
    packages=find_packages(exclude=['tests']),
    long_description=__doc__,
    include_package_data=True,
)
