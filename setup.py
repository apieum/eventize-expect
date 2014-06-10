# -*- coding: utf8 -*-
from setuptools import setup
import os

pkgName = 'eventize-expect'
setup(
    name=pkgName,
    version='0.1',
    url='http://www.python.org/pypi/' + pkgName,
    author='Grégory Salvan',
    author_email='apieum@gmail.com',
    license='LGPL',
    description='Inxpect lib util for eventize lib events',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "inxpect",
        "eventize>=0.4.3"
    ],
    entry_points = {'eventize.events': '.Expect = expect:Expect'},
    zip_safe=True,
)
