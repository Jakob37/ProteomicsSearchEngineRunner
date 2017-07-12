#!/usr/bin/env python3


import argparse
import sys

import preprocessing.main
import search.main
import postprocessing.main

VERSION = '0.1.0'

author = 'Jakob Willforss'
help_message = 'Author: {}\nVersion: {}\n\n' \
               'Automation wrapper for MSFragger' \
    .format(author, VERSION)


OPENMS_ID_CONVERTER = 'binaries/IDFileConverter'


def db_setup(args):

    preprocessing.main.preprocess_database(args)


def spectrum_setup(args):

    preprocessing.main.preprocess_spectrum(args)


def run_search(args):

    search.main.run_msfragger(args)


def post_process(args):

    postprocessing.main.main(args.input, args.output, OPENMS_ID_CONVERTER, verbose=args.verbose)


def run_all(args):

    print('Not implemented yet! Will execute all steps')
    sys.exit(1)


def parse_arguments():

    parsers = ['db_setup', 'spectrum_setup', 'run_search', 'post_process', 'run_all']

    def default_func(args):
        print('Proteomics search engine automation, version {}'.format(VERSION))
        print('\n{}'.format('\n'.join(parsers)))
        exit(1)

    parser = argparse.ArgumentParser()
    parser.set_defaults(func=default_func)

    subparsers = parser.add_subparsers(help='Commands: {}'.format(' '.join(parsers)))

    parse_db_setup(subparsers, parsers[0])
    parse_spectrum_setup(subparsers, parsers[1])
    parse_run_msfragger(subparsers, parsers[2])
    parse_postproc(subparsers, parsers[3])
    parse_run_all(subparsers, parsers[4])

    args = parser.parse_args()
    args.func(args)


def parse_run_all(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=run_all)


def parse_db_setup(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=db_setup)

    parser.add_argument('-i', '--input', help='FASTA database (default: STDIN)')
    parser.add_argument('-o', '--output', help='Prepared database (default: STDOUT)')

    parser.add_argument('-v', '--verbose', help='Output detailed diagnostic information',
                        action='store_true', default=False)


def parse_spectrum_setup(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=spectrum_setup)

    parser.add_argument('-i', '--input', help='mzML raw file (default: STDIN)')
    parser.add_argument('-o', '--output', help='mgf processed file (default: STDOUT)')

    parser.add_argument('-v', '--verbose', help='Output detailed diagnostic information',
                        action='store_true', default=False)


def parse_run_msfragger(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=run_search)

    parser.add_argument('--database', required=True, help='Fasta file containing database')
    parser.add_argument('--spectrum', required=True, help='MGF file containing spectrum to search')
    parser.add_argument('-o', '--output')

    parser.add_argument('--threads', type=int, default=1)

    parser.add_argument('--precursor_mass_tolerance', type=int, default=500)
    parser.add_argument('--precursor_mass_units', default='daltons')
    parser.add_argument('--precursor_true_tolerance', type=int, default=20)
    parser.add_argument('--precursor_true_units', default='ppm')
    parser.add_argument('--fragment_mass_tolerance', type=int, default=20)
    parser.add_argument('--fragment_mass_units', default='ppm')

    parser.add_argument('-v', '--verbose', help='Output detailed diagnostic information',
                        action='store_true', default=False)


def parse_postproc(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=post_process)

    parser.add_argument('-i', '--input', help='pepXML identification format', required=True)
    parser.add_argument('-o', '--output', help='idXML identification format', required=True)

    parser.add_argument('-v', '--verbose', help='Output detailed diagnostic information',
                        action='store_true', default=False)


if __name__ == '__main__':
    parse_arguments()
