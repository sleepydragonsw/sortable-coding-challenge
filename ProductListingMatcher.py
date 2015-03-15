#!/usr/bin/env python3

"""
ProductListingMatcher.py
By: Denver Coneybeare <denver@sleepydragon.org>
Mar 13, 2015
"""

import argparse
import logging
import os
import sys
from logging import StreamHandler


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
        super().parse_args(namespace=namespace)
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
            if not os.path.exists(products_path):
                self.parser.error("file not found: {}".format(products_path))

            listings_path = self.listings_file
            if not os.path.exists(listings_path):
                self.parser.error("file not found: {}".format(listings_path))

            logger = logging.Logger(name=__name__)
            handler = StreamHandler(sys.stdout)
            logger.addHandler(handler)

            return ProductListingMatcher(products_path, listings_path, logger)

    class Error(Exception):

        def __init__(self, message, exit_code):
            super().__init__(message)
            self.exit_code = exit_code


if __name__ == "__main__":
    try:
        exit_code = main()
    except KeyboardInterrupt:
        print("ERROR: application terminated by keyboard interrupt", file=sys.stderr)
        exit_code = 1
    sys.exit(exit_code)
