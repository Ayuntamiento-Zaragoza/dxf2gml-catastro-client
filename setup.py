# -*- coding: UTF-8 -*-

# Copyright (c) 2016-2023 Jose Antonio Chavarría <jachavar@gmail.com>
# Copyright (c) 2016-2023 Alberto Gacías <alberto@migasfree.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

__author__ = 'Alberto Gacías'
__license__ = 'GPLv3'

import sys

if not hasattr(sys, 'version_info') or sys.version_info < (3, 6, 0, 'final'):
    raise SystemExit('This project requires Python 3.6 or later.')

import os
PATH = os.path.dirname(__file__)
README = open(os.path.join(PATH, 'README.md')).read()
VERSION = open(os.path.join(PATH, 'VERSION')).read().splitlines()[0]
REQUIRES = filter(
    lambda s: len(s) > 0,
    open(os.path.join(PATH, 'requirements.txt'), encoding='utf_8').read().split('\n')
)

from setuptools import setup, find_packages


setup(
    name='dxf2gml-catastro-client',
    version=VERSION,
    description='dxf2gml_catastro_client to generate GML files from DXF',
    long_description=README,
    license='GPLv3',
    author='Alberto Gacías',
    author_email='alberto@migasfree.org',
    platforms=['Linux'],
    install_requires=REQUIRES,
    packages = find_packages(),
    scripts=['bin/dxf2gml-catastro'],
    data_files=[
        ('share/doc/dxf2gml-catastro-client', [
            'AUTHORS',
            'INSTALL',
            'LICENSE',
            'README.md',
        ]),
    ],
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
    ],
)
