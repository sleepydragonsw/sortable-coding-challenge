#!/usr/bin/env python3

"""
ProductListingMatcher.py
By: Denver Coneybeare <denver@sleepydragon.org>
Mar 13, 2015

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

import argparse
import logging
import sys


def main():
    arg_parser = ArgumentParser()
    try:
        app = arg_parser.parse_args()
    except arg_parser.Error as e:
        if e.exit_code == 2:
            print("ERROR: invalid command-line arguments: {}".format(e), file=sys.stderr)
            print("Run with --help for help", file=sys.stderr)
        elif e.exit_code != 0:
            print("ERROR: {}".format(e), file=sys.stderr)
        return e.exit_code
    else:
        try:
            app.run()
        except app.Error as e:
            print("ERROR: {}".format(e))
            return 1
        else:
            return 0


class ProductListingMatcher:

    def __init__(self, products_path, listings_path, logger):
        self.products_path = products_path
        self.listings_path = listings_path
        self.logger = logger

    def run(self):
        self.log("Reading products from file: {}".format(self.products_path))
        self.log("Reading listings from file: {}".format(self.listings_path))

    def log(self, message):
        self.logger.info(message)

    class Error(Exception):
        pass


class ArgumentParser(argparse.ArgumentParser):

    def __init__(self):
        super().__init__()
        self.add_arguments()

    def add_arguments(self):
        self.add_argument(
            "-p", "--products-file",
            default="products.txt",
            help="""The path of the file containing the products, one per line
            (default: %(default)s)"""
        )

        self.add_argument(
            "-l", "--listings-file",
            default="listings.txt",
            help="""The path of the file containing the listings, one per line
            (default: %(default)s)"""
        )

    def parse_args(self, args=None, namespace=None):
        namespace = self.Namespace(self)
        super().parse_args(args=args, namespace=namespace)
        app = namespace.create_application()
        return app

    def exit(self, status=0, message=None):
        raise self.Error(message, status)

    def error(self, message):
        self.exit(2, message)

    class Namespace(argparse.Namespace):

        def __init__(self, parser):
            self.parser = parser

        def create_application(self):
            products_path = self.products_file
            listings_path = self.listings_file

            logger = logging.Logger(name=__name__)
            handler = logging.StreamHandler(sys.stdout)
            logger.addHandler(handler)

            return ProductListingMatcher(products_path, listings_path, logger)

    class Error(Exception):

        def __init__(self, message, exit_code):
            super().__init__(message)
            self.exit_code = exit_code


class Product:

    def __init__(self, name, manufacturer, model, family, announced_date):
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.family = family
        self.announced_date = announced_date

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return (
            "Product("
            "name={0.name!r}, "
            "manufacturer={0.manufacturer!r}, "
            "model={0.model!r}, "
            "family={0.family!r}, "
            "announced_date={0.announced_date!r}"
            ")"
        ).format(self)

    def __eq__(self, other):
        try:
            other_name = other.name
            other_manufacturer = other.manufacturer
            other_model = other.model
            other_family = other.family
            other_announced_date = other.announced_date
        except AttributeError:
            return False
        else:
            return (
                other_name == self.name and
                other_manufacturer == self.manufacturer and
                other_model == self.model and
                other_family == self.family and
                other_announced_date == self.announced_date
            )

    def __ne__(self, other):
        return not self.__eq__(other)


if __name__ == "__main__":
    try:
        exit_code = main()
    except KeyboardInterrupt:
        print("ERROR: application terminated by keyboard interrupt", file=sys.stderr)
        exit_code = 1
    sys.exit(exit_code)
