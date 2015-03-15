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

import datetime
import unittest

from ProductListingMatcher import ArgumentParser
from ProductListingMatcher import Product


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


class Test_Product(unittest.TestCase):

    def test___init___PositionalArgs(self):
        name = object()
        manufacturer = object()
        model = object()
        family = object()
        announced_date = object()
        x = Product(name, manufacturer, model, family, announced_date)
        self.assertIs(x.name, name)
        self.assertIs(x.manufacturer, manufacturer)
        self.assertIs(x.model, model)
        self.assertIs(x.family, family)
        self.assertIs(x.announced_date, announced_date)

    def test___init___KeywordArgs(self):
        name = object()
        manufacturer = object()
        model = object()
        family = object()
        announced_date = object()
        x = Product(
            name=name,
            manufacturer=manufacturer,
            model=model,
            family=family,
            announced_date=announced_date,
        )
        self.assertIs(x.name, name)
        self.assertIs(x.manufacturer, manufacturer)
        self.assertIs(x.model, model)
        self.assertIs(x.family, family)
        self.assertIs(x.announced_date, announced_date)

    def test___str___(self):
        x = self.sample_object()
        actual = "{}".format(x)
        self.assertEquals(actual, "Kodak_EasyShare_M320")

    def test___repr___(self):
        x = self.sample_object()
        actual = "{!r}".format(x)
        self.assertEquals(
            actual,
            "Product(name='Kodak_EasyShare_M320', manufacturer='Kodak', model='M320', "
            "family='EasyShare', announced_date=datetime.datetime(2009, 1, 7, 0, 0))")

    def test___eq___Equal(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        self.assertTrue(o1 == o2)

    def test___eq___NotEqual_name(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.name = object()
        self.assertFalse(o1 == o2)

    def test___eq___NotEqual_manufacturer(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.manufacturer = object()
        self.assertFalse(o1 == o2)

    def test___eq___NotEqual_model(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.model = object()
        self.assertFalse(o1 == o2)

    def test___eq___NotEqual_family(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.family = object()
        self.assertFalse(o1 == o2)

    def test___eq___NotEqual_announced_date(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.announced_date = object()
        self.assertFalse(o1 == o2)

    def test___eq___NotEqual_AttributeMissing_name(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.name
        self.assertFalse(o1 == o2)

    def test___eq___NotEqual_AttributeMissing_manufacturer(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.manufacturer
        self.assertFalse(o1 == o2)

    def test___eq___NotEqual_AttributeMissing_model(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.model
        self.assertFalse(o1 == o2)

    def test___eq___NotEqual_AttributeMissing_family(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.family
        self.assertFalse(o1 == o2)

    def test___eq___NotEqual_AttributeMissing_announced_date(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.announced_date
        self.assertFalse(o1 == o2)

    def test___ne___Equal(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        self.assertFalse(o1 != o2)

    def test___ne___NotEqual_name(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.name = object()
        self.assertTrue(o1 != o2)

    def test___ne___NotEqual_manufacturer(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.manufacturer = object()
        self.assertTrue(o1 != o2)

    def test___ne___NotEqual_model(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.model = object()
        self.assertTrue(o1 != o2)

    def test___ne___NotEqual_family(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.family = object()
        self.assertTrue(o1 != o2)

    def test___ne___NotEqual_announced_date(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        o2.announced_date = object()
        self.assertTrue(o1 != o2)

    def test___ne___NotEqual_AttributeMissing_name(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.name
        self.assertTrue(o1 != o2)

    def test___ne___NotEqual_AttributeMissing_manufacturer(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.manufacturer
        self.assertTrue(o1 != o2)

    def test___ne___NotEqual_AttributeMissing_model(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.model
        self.assertTrue(o1 != o2)

    def test___ne___NotEqual_AttributeMissing_family(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.family
        self.assertTrue(o1 != o2)

    def test___ne___NotEqual_AttributeMissing_announced_date(self):
        o1 = self.sample_object()
        o2 = self.sample_object()
        del o2.announced_date
        self.assertTrue(o1 != o2)

    def sample_object(self):
        return Product(
            name="Kodak_EasyShare_M320",
            manufacturer="Kodak",
            model="M320",
            family="EasyShare",
            announced_date=datetime.datetime(2009, 1, 7),
        )


if __name__ == "__main__":
    unittest.main()
