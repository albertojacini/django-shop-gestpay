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

    'shop_gestpay.offsite_gestpay.OffsiteGestpayBackend'

to django-SHOP's SHOP_PAYMENT_BACKENDS setting.

Todo
=====

Plenty of stuff is left to do! If you feel like giving a hand, please pick a task
in the following list:

* Tests
  
Contributing
====

Feel free to post any comment or suggestion for this project on the project page
on Github.

Helpful resources
====

Gestpay documentation
____
* https://www.gestpay.it/gestpay/doc/specifiche-tecniche/starter/gestpay_specifiche_tecniche_sicurezza_con_crittografia_2_1_eng.pdf

Gestpypay (Python version of the Java Gestpay Crypt/Decrypt object)
----
* https://github.com/giefferre/gestpypay

Very similar implementation of this backend
----
* https://github.com/ninjabit/Fotomercato/tree/master/apps/gestpay

Similar django-shop payment backend plugins
----
* https://github.com/jrief/django-shop-ipayment
* https://github.com/chrisglass/django-shop-postfinance

Other
-----
* http://faustinelli.wordpress.com/2011/12/11/banca-sella-ws-for-dummies-i-web-services-di-banca-sella/
* http://stackoverflow.com/questions/115316/how-can-i-consume-a-wsdl-soap-web-service-in-python
* https://forum.sella.it/spazioaperto/posts/list/90202.page;jsessionid=CywbRq2SzDL0bj6DPvRKgyzGxJv8STS1PFhP8p66SPrbcfnt8Gzc!256069167
* https://github.com/akira28/PrestaGestpay
* http://www.mariaserenapiccioni.com/2010/10/come-criptare-i-dati-da-inviare-a-banca-sella-usando-il-webservice-wscryptdecrypt/