========================
django-shop-gestpay
========================

THIS APPLICATION IS NOT READY FOR USE YET. DON'T USE IT IN PRODUCTION!!!

This application is a Banca Sella Gestpay payment backend for django-SHOP, or any other shop
system implementing its shop interface. You can find info about the service at
https://www.gestpay.it

Usage
======

Install gestpypay::

    pip install gestpypay

Install django-shop-gestpay::

    pip install django-shop-gestpay

Add both projects to your INSTALLED_APPS.

Add::

    'shop_gestpay.offsite_gestpay.OffsiteGestpayBackend' to django-SHOP's

SHOP_PAYMENT_BACKENDS setting.

Todo
=====

Plenty of stuff is left to do! If you feel like giving a hand, please pick a task
in the following list:

* Tests
  
Contributing
=============

Feel free to post any comment or suggestion for this project on the project page
on Github.