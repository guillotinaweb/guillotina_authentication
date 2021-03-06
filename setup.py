from setuptools import find_packages
from setuptools import setup


try:
    README = open('README.rst').read()
except IOError:
    README = ''

try:
    README += '\n\n' + open('CHANGELOG.rst').read()
except IOError:
    pass

setup(
    name='guillotina_authentication',
    version=open('VERSION').read().strip(),
    description='Authenticate Guillotina with various providers',
    long_description=README,
    install_requires=[
        'guillotina>=5.0.0a10',
        'aioauth-client'
    ],
    author='Nathan Van Gheem',
    author_email='vangheem@gmail.com',
    url='',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    },
    classifiers=[],
    entry_points={
    }
)
