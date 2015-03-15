#!/usr/bin/env python3

"""
ProductListingMatcher_test.py
By: Denver Coneybeare <denver@sleepydragon.org>
Mar 15, 2015

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import unittest

from ProductListingMatcher import ArgumentParser

class Test_ArgumentParser(unittest.TestCase):

    def test_NoArgumentsSpecified(self):
        x = ArgumentParser()
        result = x.parse_args(args=[])
        self.assertEquals(result.products_path, "products.txt")
        self.assertEquals(result.listings_path, "listings.txt")

    def test_ListingsFileSpecified_short(self):
        x = ArgumentParser()
        result = x.parse_args(args=["-l", "test_listings.txt"])
        self.assertEquals(result.products_path, "products.txt")
        self.assertEquals(result.listings_path, "test_listings.txt")

    def test_ListingsFileSpecified_long(self):
        x = ArgumentParser()
        result = x.parse_args(args=["--listings-file", "test_listings.txt"])
        self.assertEquals(result.products_path, "products.txt")
        self.assertEquals(result.listings_path, "test_listings.txt")

    def test_ProductsFileSpecified_short(self):
        x = ArgumentParser()
        result = x.parse_args(args=["-p", "test_products.txt"])
        self.assertEquals(result.products_path, "test_products.txt")
        self.assertEquals(result.listings_path, "listings.txt")

    def test_ProductsFileSpecified_long(self):
        x = ArgumentParser()
        result = x.parse_args(args=["-p", "test_products.txt"])
        self.assertEquals(result.products_path, "test_products.txt")
        self.assertEquals(result.listings_path, "listings.txt")
