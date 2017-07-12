from search.params_template import PARAMS_TEMPLATE

PARAM_FP = 'params/msfragger.param'


def run_msfragger(args):

    params_file_string = generate_params_file_string(PARAMS_TEMPLATE,
                                                     args.database,
                                                     threads=args.threads,
                                                     precursor_mass_tolerance=args.precursor_mass_tolerance,
                                                     precursor_mass_units=args.precursor_mass_units,
                                                     precursor_true_tolerance=args.precursor_true_tolerance,
                                                     precursor_true_units=args.precursor_true_units,
                                                     fragment_mass_tolerance=args.fragment_mass_tolerance,
                                                     fragment_mass_units=args.fragment_mass_units)

    with open(PARAM_FP, 'w') as out_fh:
        out_fh.write(params_file_string)


def setup_command_list():
    pass


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

