import unittest
import requests
import pytest
import requests_mock

from flask import url_for
from flask_testing import TestCase

from app import app

from application.routes import prime 


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        print("-----------")

    def tearDown(self):
        print("--------")


class TestPrime(unittest.TestCase):

    def test_values(self):

        self.assertEqual(prime(11), 'prime', msg='Equal')
        self.assertEqual(prime(15), 'composite', msg='Equal')
        self.assertEqual(prime(1), 'You do not appear to exist', msg='Equal')
        self.assertEqual(prime(2), 'prime', msg='Equal')
        self.assertEqual(prime(3), 'prime', msg='Equal')
        self.assertEqual(prime(4), 'composite', msg='Equal')
        self.assertEqual(prime(121), 'composite', msg='Equal')
        self.assertEqual(prime(233), 'prime', msg='Equal')
        self.assertEqual(prime(7901), 'prime', msg='Equal')
        self.assertEqual(prime(7903), 'composite', msg='Equal')
      


        
        
        