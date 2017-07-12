import preprocessing.database
import preprocessing.spectrum
import search.main
import postprocessing.main


def main(args):

    raw_database = args.database
    processed_database = '{}.processed'.format(raw_database)

    spectrum = args.spectrum
    threads = args.threads
    verbose = args.verbose

    spectrum_base = '.'.join(spectrum.split('.')[:-1])

    msfragger_result = spectrum_base + '.pepXML'
    formatted_result = spectrum_base + '.idXML'

    print('Preprocessing database')
    preprocessing.database.main(raw_database, processed_database, args.verbose)

    print('Executing MSFragger run')
    search.main.run_msfragger(database_fp=processed_database,
                              spectrum_fp=spectrum,
                              threads=threads,
                              precursor_mass_tolerance=args.precursor_mass_tolerance,
                              precursor_mass_units=args.precursor_mass_units,
                              precursor_true_tolerance=args.precursor_true_tolerance,
                              precursor_true_units=args.precursor_true_units,
                              fragment_mass_tolerance=args.fragment_mass_tolerance,
                              fragment_mass_units=args.fragment_mass_units,
                              verbose=verbose)

    print('Parsing MSFragger output')
    postprocessing.main.main(msfragger_result, formatted_result)

    print('All done!')
