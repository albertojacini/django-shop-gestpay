#-*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

CLASSIFIERS = []

setup(
    author="Alberto Jacini",
    author_email="albertojacini@gmail.com",
    name='django-shop-gestpay',
    version='0.0.3',
    description='A Gestpay payment backend',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='http://www.django-shop.org/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.4',
    ],
    packages=find_packages(exclude=["example", "example.*"]),
    zip_safe = False
)
