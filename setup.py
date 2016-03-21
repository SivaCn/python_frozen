# -*- coding: utf-8 -*-

from setuptools import setup


setup(
	name='frozen',
	description='Get a python_frozen reference to an object.',
	long_description='',
	url='https://github.com/mverleg/python_frozen',
	author='Mark V',
	maintainer='(the author)',
	author_email='mdilligaf@gmail.com',
	license='LICENSE.txt',
	keywords=[],
	version='1.0',
	packages=[
		'python_frozen',
	],
	include_package_data=True,
	zip_safe=False,
	requires=[
		'lazy-object-proxy',
	],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)


