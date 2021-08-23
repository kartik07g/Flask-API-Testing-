import unittest

import mysql
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
from main import Inject,  app

class test_result(Inject, unittest.TestCase):
    def test_result1(self):

        user = "kartik07g"
        password = "k123"
        c1 = Inject()
        val = c1.check(user, password)

        self.assertTrue(val)


if __name__ == '__main__':
    unittest.main()
