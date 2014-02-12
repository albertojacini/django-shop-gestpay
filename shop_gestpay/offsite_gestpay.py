#-*- coding: utf-8 -*-
import logging

from shop.payment.api import PaymentAPI
import gestpypay

from django.conf import settings
from django.conf.urls.defaults import patterns, url
from django.http import (HttpResponseBadRequest, HttpResponse, HttpResponseRedirect)
from django.template.context import RequestContext
from django.shortcuts import render_to_response


class OffsiteGestpayBackend(object):
    '''
    Glue code to let django-SHOP talk to django-paypal's.

    The django-paypal package already defines an IPN view, that logs everything
    to the database (desirable), and fires up a signal.
    It is therefore more convenient to listen to the signal instead of rewriting
    the ipn view (and necessary tests)
    '''

    backend_name = "Carta di credito - Banca Sella Gestpay"
    url_namespace = "gestpay_banca_sella"

    shop_login = settings.GESTPAY_SHOP_LOGIN
    currency_code = settings.GESTPAY_CURRENCY_CODE
    server = settings.GESTPAY_SERVER

    def __init__(self, shop):
        self.shop = shop
        self.logger = logging.getLogger(__name__)

        assert settings.GESTPAY_SHOP_LOGIN, "You need to define a GESTPAY_SHOP_LOGIN in settings."
        assert settings.GESTPAY_CURRENCY_CODE, "You need to define a GESTPAY_CURRENCY_CODE in settings."
        assert settings.GESTPAY_SERVER, """You need to define a GESTPAY_SERVER in settings.
                                        Set 'testecomm.sella.it' for test and 'ecomm.sella.it'
                                         for production."""

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.view_that_asks_for_money, name='gestpay_banca_sella'),
            # The complete url: http://iperborea.com/iperboreastore/pay/gestpay_banca_sella/transaction_result_response/
            url(r'^transaction_result_response/$', self.get_transaction_result_response, name='gestpay_transaction_result_response'),
            url(r'^error/$', self.gestpay_error_view, name='gestpay_error'),
            url(r'^success/$', self.gestpay_success_view, name='gestpay_success')
        )
        return urlpatterns

    # The following are the Gestpay views
    def view_that_asks_for_money(self, request):
        """
        1. The buyer selects the items to buy and decides to preceed with payment.
        2. The merchant's server contacts GestPay sever via the Internet to
        encrypt the payment transaction data.
        """
        order = self.shop.get_order(request)
        order_id = self.shop.get_order_unique_id(order)
        amount = self.shop.get_order_total(order)
        transaction_id = str(order_id) # Would it be better to create a more talkative code?
        custom_parameters = "" # See Gestpay documentation

        # Instantiate Gestpay payment handler (gph)
        gph = gestpypay.GestPayCrypt()
        gph.Debug = settings.DEBUG
        gph.ProtocolAuthServer = 'https'
        gph.DomainName = self.server

        gph.SetShopLogin(self.shop_login)
        gph.SetCurrency(self.currency_code)

        gph.SetAmount(amount)
        gph.SetShopTransactionID(transaction_id)

        gph.SetCustomInfo(custom_parameters)

        if gph.Encrypt():
            checkout_action_url = "%s://%s/gestpay/pagam.asp" % (gph.ProtocolAuthServer, gph.DomainName)
            shop_login = gph.GetShopLogin()
            encrypted_string = gph.GetEncryptedString()
        else:
            print gph.GetErrorCode()
            print gph.GetErrorDescription()
    
        context = RequestContext(request, {
           'shop_login': self.shop_login,
           'encrypted_string': encrypted_string,
           'checkout_action_url': checkout_action_url
        })
        return render_to_response("shop_gestpay/payment.html", context)

    def get_transaction_result_response(self, request):
        """
        6. GestPay communicates to the merchant's server an encrypted parameter
        string which returns the result of the transaction.
        7a. The merchant's server contacts the GestPay server via Internet to
        decrypt the encrypted data string which reurns the result of the
        transaction.
        """
        shop_login = request.GET['a']
        string_to_be_decrypted = request.GET['b']
        self.logger.info('Gestpay sent back the string %s to be decrypted.', string_to_be_decrypted)

        # Decrypt
        gph = gestpypay.GestPayCrypt()
        gph.SetEncryptedString(string_to_be_decrypted)
        gph.SetShopLogin(self.shop_login)
        gph.DomainName = self.server
        response = gph.Decrypt()
        if response == 1:
            logging.info('Response from Gestpay: %s ; shopid = %s ; enc_string = %s' % (
                            gph.GetTransactionResult(), gph.GetShopLogin(), gph.GetEncryptedString()))
            order_id = gph.GetShopTransactionID()
            order = self.shop.get_order_for_id(order_id)  # Get the order from either the POST or the GET parameters
            amount = gph.GetAmount()
            bank_transaction_id = gph.GetBankTransactionID()
            # This actually records the payment in the shop's database
            self.shop.confirm_payment(order, amount, bank_transaction_id, self.backend_name)
            # Respond to Gestpay
            return HttpResponse('Ok')
        else:
            logging.error('Response from Gestpay Error: %s ; shopid = %s ; enc_string = %s' % (
                            gph.GetErrorDescription(), gph.GetShopLogin(), gph.GetEncryptedString()))
            return HttpResponseBadRequest()


    def gestpay_error_view(self, request):
        """

        """
        return render_to_response('shop_gestpay/error.html', request)

    def gestpay_success_view(self, request):
        return HttpResponseRedirect(self.shop.get_finished_url())