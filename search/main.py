from search.params_template import PARAMS_TEMPLATE
from utils import utils

PARAM_FP = 'params/msfragger.param'
MSFRAGGER_PATH = 'binaries/MSFragger.jar'
MSFRAGGER_COMMAND_TEMPLATE = 'java -jar {binary_fp} {param} {mzml}'


def run_msfragger(database_fp, spectrum_fp, threads, precursor_mass_tolerance,
                  precursor_mass_units, precursor_true_tolerance,
                  precursor_true_units, fragment_mass_tolerance,
                  fragment_mass_units, verbose):

    params_file_string = generate_params_file_string(PARAMS_TEMPLATE,
                                                     database_fp,
                                                     threads=threads,
                                                     precursor_mass_tolerance=precursor_mass_tolerance,
                                                     precursor_mass_units=precursor_mass_units,
                                                     precursor_true_tolerance=precursor_true_tolerance,
                                                     precursor_true_units=precursor_true_units,
                                                     fragment_mass_tolerance=fragment_mass_tolerance,
                                                     fragment_mass_units=fragment_mass_units)

    with open(PARAM_FP, 'w') as out_fh:
        out_fh.write(params_file_string)

    command_list = setup_command_list(MSFRAGGER_PATH, PARAM_FP, spectrum_fp)

    print('--- Executing MSFragger ---')
    utils.run_command(command_list, verbose=verbose)
    print('--- MSFragger processing done! ---')


def setup_command_list(binary_fp, param_fp, mzml_fp):

    command_string = MSFRAGGER_COMMAND_TEMPLATE.format(binary_fp=binary_fp,
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
