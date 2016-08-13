#!/usr/bin/env python3
# vim: set encoding=utf-8 tabstop=4 softtabstop=4 shiftwidth=4 expandtab
#########################################################################
# Copyright 2016 Christian Strassburg  c.strassburg@gmx.de
#########################################################################
#  This file is part of SmartHomeNG
#  https://github.com/smarthomeNG/smarthome
#  http://knx-user-forum.de/
#
#  SmartHomeNG is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SmartHomeNG is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SmartHomeNG If not, see <http://www.gnu.org/licenses/>.
#########################################################################
import common
import unittest
from lib.utils import Utils
#from wakeonlan import WakeOnLan
class LibUtilsTest(unittest.TestCase):

    def test_is_mac(self):
        self.assertTrue(True)
        self.assertTrue(Utils.is_mac("11:22:33:44:55:66"))
        self.assertTrue(Utils.is_mac("11-22-33-44-55-66"))
        self.assertTrue(Utils.is_mac("11 22 33 44 55 66"))
        self.assertTrue(Utils.is_mac("112233445566"))
        self.assertTrue(Utils.is_mac("000000000000"))
        self.assertTrue(Utils.is_mac("ffffffffffff"))
        self.assertFalse(Utils.is_mac("1r2233445566"))
        self.assertFalse(Utils.is_mac("gggggggggggg"))
        self.assertFalse(Utils.is_mac("1g:22:33:44:55:66"))
        self.assertFalse(Utils.is_mac(None))
        self.assertFalse(Utils.is_mac(""))
        self.assertFalse(Utils.is_mac(self))

    def test_is_ip(self):
        self.assertFalse(Utils.is_ip(""))
        self.assertFalse(Utils.is_ip(None))
        self.assertFalse(Utils.is_ip(self))

        self.assertTrue(Utils.is_ip("1.2.3.4"))
        self.assertTrue(Utils.is_ip("0.0.0.0"))
        self.assertTrue(Utils.is_ip("255.255.255.255"))
        self.assertFalse(Utils.is_ip("256.256.256.256"))
        self.assertFalse(Utils.is_ip("2561.256.256.256"))
        self.assertFalse(Utils.is_ip("561.256.256.256"))
        self.assertFalse(Utils.is_ip("161.256.256"))
        self.assertTrue(Utils.is_ip("10.0.0.173"))

    def test_is_int(self):
        self.assertFalse(Utils.is_int(""))
        self.assertFalse(Utils.is_int(None))
        self.assertFalse(Utils.is_int(self))

        self.assertFalse(Utils.is_int("1.2.3.4"))
        self.assertFalse(Utils.is_int("xyzabcd"))
        self.assertFalse(Utils.is_int("1.0"))
        self.assertTrue(Utils.is_int("255"))
        self.assertTrue(Utils.is_int("0"))
        self.assertTrue(Utils.is_int("-1"))

    def test_is_float(self):
        self.assertFalse(Utils.is_float(""))
        self.assertFalse(Utils.is_float(None))
        self.assertFalse(Utils.is_float(self))

        self.assertFalse(Utils.is_float("1.2.3.4"))
        self.assertFalse(Utils.is_float("xyzabcd"))
        self.assertTrue(Utils.is_float("255"))
        self.assertTrue(Utils.is_float("0"))
        self.assertTrue(Utils.is_float("-1"))
        self.assertTrue(Utils.is_float("1.0"))
        self.assertTrue(Utils.is_float("0.0"))
        self.assertTrue(Utils.is_float("5.0"))
        self.assertTrue(Utils.is_float("-5.0"))
        self.assertTrue(Utils.is_float("2.01"))
        self.assertTrue(Utils.is_float("-2.01"))

    def test_to_bool(self):
        with self.assertRaises(Exception):
            Utils.to_bool("161.256.256")
        
       # with self.assertRaises(Exception):
       #     Utils.to_bool(self)
        self.assertFalse(Utils.to_bool(None))
        self.assertFalse(Utils.to_bool(False))
        self.assertFalse(Utils.to_bool("No"))
        self.assertFalse(Utils.to_bool("0"))
        self.assertFalse(Utils.to_bool(""))
        self.assertFalse(Utils.to_bool("n"))
        self.assertFalse(Utils.to_bool("false"))
        self.assertFalse(Utils.to_bool("False"))
        self.assertFalse(Utils.to_bool("f"))
        self.assertFalse(Utils.to_bool(0))

        self.assertTrue(Utils.to_bool(1.2))
        self.assertTrue(Utils.to_bool(True))
        self.assertTrue(Utils.to_bool("yes"))
        self.assertTrue(Utils.to_bool("1"))
        self.assertTrue(Utils.to_bool("y"))
        self.assertTrue(Utils.to_bool("true"))
        self.assertTrue(Utils.to_bool("True"))
        self.assertTrue(Utils.to_bool("t"))
        self.assertTrue(Utils.to_bool(1))

    def test_create_hash(self):
        with self.assertRaises(Exception):
            Utils.create_hash(None)
        self.assertEqual(Utils.create_hash(''), 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e')
        self.assertEqual(Utils.create_hash('42'), '39ca7ce9ecc69f696bf7d20bb23dd1521b641f806cc7a6b724aaa6cdbffb3a023ff98ae73225156b2c6c9ceddbfc16f5453e8fa49fc10e5d96a3885546a46ef4')
        self.assertEqual(Utils.create_hash('very_secure_password'), '1245a9633edf47b7091f37c4d294b5be5a9936c81c5359b16d1c4833729965663f1943ef240959c53803fedef7ac19bd59c66ad7e7092d7dbf155ce45884607d')
        self.assertEqual(Utils.create_hash('1245a9633edf47b7091f37c4d294b5be5a9936c81c5359b16d1c4833729965663f1943ef240959c53803fedef7ac19bd59c66ad7e7092d7dbf155ce45884607d'), '00faf4a142f087e55edf6e91ea333d9a4bcd9b2d6bba8fab42869c6e00e28a3acba6d5fe3495f037221d633e01b3c7baa6e915028407548f77b5b9710899bfbe')

if __name__ == '__main__':
    unittest.main(verbosity=2)
