#-*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Topic :: Other/Nonlisted Topic'
]

setup(
    author="Alberto Jacini",
    author_email="albertojacini@gmail.com",
    name='django-shop-gestpay',
    version='0.0.1',
    description='A Banca Sella Gestpay payment backend',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
        url='https://github.com/albertojacini/django-shop-gestpay',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'django>=1.4',
        'django-shop',
        'gestpypay'
    ],
    packages=find_packages(),
    zip_safe=False
)
