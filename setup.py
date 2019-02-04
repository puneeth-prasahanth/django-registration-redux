import sys,os
import setuptools
import registration
from registration import get_version
from setuptools import find_packages
from setuptools import setup
from setuptools.command.test import test as TestCommand

##############
#VERSION = (1, 1, 0, 'final', 0)
#
#
#def get_version():
#    "Returns a PEP 386-compliant version number from VERSION."
#    assert len(VERSION) == 5
#    assert VERSION[3] in ('alpha', 'beta', 'rc', 'final')
#
#    # Now build the two parts of the version number:
#    # main = X.Y[.Z]
#    # sub = .devN - for pre-alpha releases
#    #     | {a|b|c}N - for alpha, beta and rc releases
#
#    parts = 2 if VERSION[2] == 0 else 3
#    main = '.'.join(str(x) for x in VERSION[:parts])
#
#    sub = ''
#    if VERSION[3] != 'final':
#        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
#        sub = mapping[VERSION[3]] + str(VERSION[4])
#
#    return str(main + sub)
#
#############




setup(name="django-registration-redux",
                 version=get_version().replace(' ', '-'),
                 author='puneeth prashnath',
                author_email='puneeth.prashant@gmail.com',
                url='https://github.com/puneeth-prasahanth/django-registration-redux',
                package_dir={'registration': 'registration'},
                packages=find_packages(),

                  include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],)




