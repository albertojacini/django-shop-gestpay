# -*- coding: utf-8 -*-
import gestpypay

from django.test.testcases import TestCase
from django.conf import settings

class GestpayTestCase(TestCase):

    def setUp(self):
        """
        1. The buyer selects the items to buy and decides to preceed with payment.
        2. The merchant's server contacts GestPay sever via the Internet to
        encrypt the payment transaction data.
        """
        self.shop_login = settings.GESTPAY_SHOP_LOGIN
        self.currency_code = settings.GESTPAY_CURRENCY_CODE
        self.order_id = 1
        self.amount = 0.01
        self.transaction_id = u'TEST00_ID' + str(self.order_id)
        self.custom_parameters = ""
    
        self.sella_payment_handler = gestpypay.GestPayCrypt()
    
        self.sella_payment_handler.Debug = True
        self.sella_payment_handler.ProtocolAuthServer = 'https'
        self.sella_payment_handler.DomainName = 'testecomm.sella.it'

        self.sella_payment_handler.SetShopLogin(self.shop_login)
        self.sella_payment_handler.SetCurrency(self.currency_code)
        self.sella_payment_handler.SetAmount(self.amount)
        self.sella_payment_handler.SetShopTransactionID(self.transaction_id)

        self.sella_payment_handler.SetCustomInfo(self.custom_parameters)

        if self.sella_payment_handler.Encrypt():
            checkout_action_url = "%s://%s/gestpay/pagam.asp" % (self.sella_payment_handler.ProtocolAuthServer, self.sella_payment_handler.DomainName)
            shop_login = self.sella_payment_handler.GetShopLogin()
            encrypted_string = self.sella_payment_handler.GetEncryptedString()
        else:
            print self.sella_payment_handler.GetErrorCode()
            print self.sella_payment_handler.GetErrorDescription()

    def test_encryption(self):
        self.assertEqual(self.sella_payment_handler.Encrypt(), 1)