import os
import sys

from modules import utils
from modules.params_template import PARAMS_TEMPLATE

PARAM_FP = 'params/msfragger.param'
MSFRAGGER_COMMAND_TEMPLATE = 'java -jar {msfragger_jar} {param} {mzml}'


def run_msfragger(msfragger_jar, database_fp, spectrum_fp, out_fp, threads, precursor_mass_tolerance,
                  precursor_mass_units, precursor_true_tolerance,
                  precursor_true_units, fragment_mass_tolerance,
                  fragment_mass_units, verbose, force=False):

    orig_out_fp = get_original_output_fp(spectrum_fp)
    if not force and os.path.isfile(orig_out_fp):
        print('ERROR: Output file at {} would be overwritten, stopping. --force to overwrite.'
              .format(orig_out_fp))
        sys.exit(1)

    params_file_string = generate_params_file_string(PARAMS_TEMPLATE,
                                                     database_fp,
                                                     threads=threads,
                                                     precursor_mass_tolerance=precursor_mass_tolerance,
                                                     precursor_mass_units=precursor_mass_units,
                                                     precursor_true_tolerance=precursor_true_tolerance,
                                                     precursor_true_units=precursor_true_units,
                                                     fragment_mass_tolerance=fragment_mass_tolerance,
                                                     fragment_mass_units=fragment_mass_units)

    print('#####  Writing parameter file to {}  #####'.format(PARAM_FP))
    with open(PARAM_FP, 'w') as out_fh:
        out_fh.write(params_file_string)

    command_list = setup_command_list(msfragger_jar, PARAM_FP, spectrum_fp)
    utils.run_command(command_list, verbose=verbose)

    if not os.path.isfile(orig_out_fp):
        print('ERROR: Output file not found at expected location: {}, did the run fail?'.format(orig_out_fp))
        sys.exit(1)

    print('Moving output {} to designated location {}'.format(orig_out_fp, out_fp))
    os.rename(orig_out_fp, out_fp)


def get_original_output_fp(in_fp):

    original_path = '.'.join(in_fp.split('.')[:-1]) + '.pepXML'
    return original_path


def setup_command_list(msfragger_jar, param_fp, mzml_fp):

    command_string = MSFRAGGER_COMMAND_TEMPLATE.format(msfragger_jar=msfragger_jar,
                                                       param=param_fp,
                                                       mzml=mzml_fp)

    return command_string.split(' ')


def generate_params_file_string(template, database,
                                threads=1,
                                precursor_mass_tolerance=500,
                                precursor_mass_units='daltons',
                                precursor_true_tolerance=20,
                                precursor_true_units='ppm',
                                fragment_mass_tolerance=20,
                                fragment_mass_units='ppm'):

    precursor_mass_units_int = get_mass_unit_from_string(precursor_mass_units)
    precursor_true_units_int = get_mass_unit_from_string(precursor_true_units)
    fragment_mass_units_int  = get_mass_unit_from_string(fragment_mass_units)

    prepared_template = template.format(database=database,
                                        threads=threads,
                                        precursor_mass_tolerance=precursor_mass_tolerance,
                                        precursor_mass_units_int=precursor_mass_units_int,
                                        precursor_true_tolerance=precursor_true_tolerance,
                                        precursor_true_units_int=precursor_true_units_int,
                                        fragment_mass_tolerance=fragment_mass_tolerance,
                                        fragment_mass_units_int=fragment_mass_units_int)

    return prepared_template


def get_mass_unit_from_string(mass_string):

    if mass_string == 'daltons':
        return 0
    elif mass_string == 'ppm':
        return 1
    else:
        raise ValueError('Unknown mass string: {}, only accepted are "daltons" and "ppm"')

