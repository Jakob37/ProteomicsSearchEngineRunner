#!/usr/bin/env python3


import argparse

VERSION = '0.1.0'

author = 'Jakob Willforss'
help_message = 'Author: {}\n Version: {}\n\n' \
               'Automation wrapper for MSFragger' \
    .format(author, VERSION)


def db_setup():
    pass


def run_search():
    pass


def post_process():
    pass


def run_all():
    pass


def parse_arguments():

    parsers = ['db_setup', 'run_search', 'post_process', 'run_all']

    def default_func(args):
        print('Proteomics search engine automation, version {}'.format(VERSION))
        print('\n{}'.format('\n'.join(parsers)))
        exit(1)

    parser = argparse.ArgumentParser()
    parser.set_defaults(func=default_func)

    subparsers = parser.add_subparsers(help='Commands: {}'.format(' '.join(parsers)))

    parse_db_setup(subparsers, parsers[0])


def parse_run_all(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=db_setup)


def parse_db_setup(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=db_setup)


def parse_run_msfragger(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=db_setup)


def parse_postproc(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=db_setup)


if __name__ == '__main__':
    parse_arguments()
