#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools, os.path as path

with open('README.md', 'r+') as f: description = f.read().strip()
with open('data/split_symbol', 'r+') as f: split_symbol = f.read().strip()
with open('data/description', 'r+') as f: description_short = f.read().strip()
with open('data/version', 'r+') as f: version = f.read().strip()
with open('data/author', 'r+') as f: author = f.read().strip()
with open('data/dependency', 'r+') as f: dependencies = f.read().strip().split(split_symbol)
with open('data/python_version', 'r+') as f: python_version = f.read().strip()

module_name = path.basename(path.dirname(__file__))

setuptools.setup(
    name = module_name,
    version = version,
    author = author,
    description = description_short,
    long_description = description,
    long_description_content_type = 'text/markdown',
    py_modules = [module_name],
    install_requires = dependencies,
    packages = setuptools.find_packages(),
    python_requires = python_version
)