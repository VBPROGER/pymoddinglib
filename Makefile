SHELL := /usr/bin/env bash
.SILENT: sinstall sbuild sclean stest

sinstall:
	echo 'Starting installation'
	python3 -m pip install .
sbuild:
	echo 'Starting build'
	python3 -m pip install --user --upgrade setuptools wheel
	python3 setup.py sdist bdist_wheel
sclean:
	echo 'Starting to clean'
	rm -rf *.o
	rm -rf __pycache__
	rm -rf build
	rm -rf dist
	rm -rf *.egg
	rm -rf *.egg-info
stest:
	echo 'Starting tests'
	python3 test/test.py
