# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license_content = f.read()

excluded = []


def exclude_package(pkg):
    for exclude in excluded:
        if pkg.startswith(exclude):
            return True
    return False


def create_package_list(base_package):
    return ([base_package] +
            [base_package + '.' + pkg
             for pkg
             in find_packages(base_package)
             if not exclude_package(pkg)])

setup(
    name='barcode-lib',
    version='0.0.1',
    description='A Python utility for generating barcode to a PDF.',
    long_description=readme,
    author='Neyvis Remon',
    author_email='neyvis.remon.gonzalez@gmail.com',
    url='https://github.com/neyvis/barcode-lib',
    license=license_content,
    packages=create_package_list('barcodelib'),
    install_requires=[
        "reportlab>=3.3.0",
    ],
    keywords=["barcode", ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
