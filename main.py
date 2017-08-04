#!/usr/bin/env python3


import argparse

import modules.database
import modules.run_search
import modules.postprocessing
import modules.runall
import modules.spectrum

VERSION = '0.1.0'

author = 'Jakob Willforss'
help_message = 'Author: {}\nVersion: {}\n\n' \
               'Automation wrapper for MSFragger' \
    .format(author, VERSION)


def db_setup(args):

    modules.database.preprocess_database(args)


def spectrum_setup(args):

    modules.spectrum.preprocess_spectrum(args)


def run_search(args):

    modules.run_search.run_msfragger(msfragger_jar=args.msfragger_jar,
                                     database_fp=args.database,
                                     spectrum_fp=args.input,
                                     out_fp=args.output,
                                     threads=args.threads,
                                     precursor_mass_tolerance=args.precursor_mass_tolerance,
                                     precursor_mass_units=args.precursor_mass_units,
                                     precursor_true_tolerance=args.precursor_true_tolerance,
                                     precursor_true_units=args.precursor_true_units,
                                     fragment_mass_tolerance=args.fragment_mass_tolerance,
                                     fragment_mass_units=args.fragment_mass_units,
                                     min_charge=args.min_charge,
                                     max_charge=args.max_charge,
                                     verbose=args.verbose,
                                     force=args.force)


def post_process(args):

    modules.postprocessing.main(args.input, args.output, args.openms_bin, verbose=args.verbose)


def run_all(args):

    modules.runall.main(args)


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

    parser.add_argument('--database', '--db', help='FASTA formatted protein database')
    parser.add_argument('--spectrum', '--input', '-i', help='Search spectrum in mzML format')
    parser.add_argument('--threads', type=int, default=1)
    parser.add_argument('--output', '-o')

    parser.add_argument('--openms_bin', help='Path to OpenMS binary files', required=True)
    parser.add_argument('--msfragger_jar', help='Path to MSFragger jar-file', required=True)

    parser.add_argument('--precursor_mass_tolerance', type=int, default=500)
    parser.add_argument('--precursor_mass_units', default='daltons')
    parser.add_argument('--precursor_true_tolerance', type=int, default=20)
    parser.add_argument('--precursor_true_units', default='ppm')
    parser.add_argument('--fragment_mass_tolerance', type=int, default=20)
    parser.add_argument('--fragment_mass_units', default='ppm')

    parser.add_argument('-v', '--verbose', help='Output detailed diagnostic information',
                        action='store_true', default=False)


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

    parser.add_argument('--openms_bin', help='Path to OpenMS binaries directory', required=True)

    parser.add_argument('-v', '--verbose', help='Output detailed diagnostic information',
                        action='store_true', default=False)


def parse_run_msfragger(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=run_search)

    parser.add_argument('--input', '-i', '--spectrum', required=True, help='MGF file containing spectrum to search')
    parser.add_argument('-o', '--output')
    parser.add_argument('--database', '--db', required=True, help='Fasta file containing database')

    parser.add_argument('--threads', type=int, default=1)

    parser.add_argument('--msfragger_jar', help='Path to MSFragger jar-file', required=True)

    parser.add_argument('--precursor_mass_tolerance', type=int, default=500)
    parser.add_argument('--precursor_mass_units', default='daltons')
    parser.add_argument('--precursor_true_tolerance', type=int, default=20)
    parser.add_argument('--precursor_true_units', default='ppm')
    parser.add_argument('--fragment_mass_tolerance', type=int, default=20)
    parser.add_argument('--fragment_mass_units', default='ppm')

    parser.add_argument('--min_charge', type=int, default=0, help='Leave min at 0 for no filtering')
    parser.add_argument('--max_charge', type=int, default=0)

    parser.add_argument('--force', help='Force overwrite if output exists', default=False, action='store_true')

    parser.add_argument('-v', '--verbose', help='Output detailed diagnostic information',
                        action='store_true', default=False)


def parse_postproc(subparsers, parser_name):

    parser = subparsers.add_parser(parser_name)
    parser.set_defaults(func=post_process)

    parser.add_argument('-i', '--input', help='pepXML identification format', required=True)
    parser.add_argument('-o', '--output', help='idXML identification format', required=True)

    parser.add_argument('--openms_bin', help='Path to OpenMS binaries', required=True)

    parser.add_argument('-v', '--verbose', help='Output detailed diagnostic information',
                        action='store_true', default=False)


if __name__ == '__main__':
    parse_arguments()
