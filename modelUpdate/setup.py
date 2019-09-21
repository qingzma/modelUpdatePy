# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='modelupdate',
    version='0.0.1',
    description='model update strategy.',
    classifiers=[
        'Development Status :: 0.0.1',
        'License :: OSI Approved :: Apache License 2.0',
        'Programming Language :: Python :: 3.6',
        'Topic :: Approximate Query Processing :: AQP :: Data Warehouse',
      ],
    keywords='Approximate Query Processing AQP',
    url='https://github.com/qingzma/DBEstClient',
    author='Qingzhi Ma',
    author_email='Q.Ma.2@warwick.ac.uk',
    long_description=readme,
    license='Apache License 2.0',#license,
    packages=['modelupdate'], #find_packages(exclude=('examples', 'docs')),
    entry_points = {
            'console_scripts': ['modelupdate=modelupdate.main:main'],
        },
    zip_safe=False,
    install_requires=[
          'numpy','pandas','scikit-learn', 'scipy'
      ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
