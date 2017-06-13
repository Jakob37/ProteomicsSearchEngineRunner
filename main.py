#!/usr/bin/env python3


import argparse

import preprocessing.main
import search.main
import postprocessing.main

VERSION = '0.1.0'

author = 'Jakob Willforss'
help_message = 'Author: {}\n Version: {}\n\n' \
               'Automation wrapper for MSFragger' \
    .format(author, VERSION)


def db_setup(args):

    preprocessing.main.main(args)


def run_search(args):

    search.main.main(args)


def post_process(args):

    postprocessing.main.main(args)


def run_all(args):

    preprocessing.main.main(args)
    search.main.main(args)
    postprocessing.main.main(args)


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
    parse_run_msfragger(subparsers, parsers[1])
    parse_postproc(subparsers, parsers[2])
    parse_run_all(subparsers, parsers[3])

    args = parser.parse_args()
    args.func(args)


def parse_run_all(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=run_all)


def parse_db_setup(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=db_setup)

    parser.add_argument('--input', help='FASTA database (default: STDIN)')
    parser.add_argument('--output', help='Prepared database (default: STDOUT)')

    parser.add_argument('--verbose', help='Output detailed diagnostic information',
                        action='store_true', default=False)


def parse_run_msfragger(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=run_search)


def parse_postproc(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=post_process)


if __name__ == '__main__':
    parse_arguments()
