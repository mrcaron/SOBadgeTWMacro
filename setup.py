#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name = 'TracStackOverflowBadge',
    version = '1.0',
    packages = ['sobadge'],
    #package_data = { 'sobadge': ['templates/*.cs', 'htdocs/*.js', 'htdocs/*.css' ] },

    author = 'Michael Caron',
    author_email = 'mike@cruxus.com',
    description = 'A Trac wiki macro to display SO badges.',
    license = 'BSD',
    keywords = 'trac plugin macro stackoverflow badge',
    #url = 'http://trac-hacks.org/wiki/OhlohBadgeMacro',
    classifiers = [
        'Framework :: Trac',
    ],
    
    install_requires = [],

    entry_points = {
        'trac.plugins': [
            'sobadge.macro = sobadge.macro',
        ]
    },
)
