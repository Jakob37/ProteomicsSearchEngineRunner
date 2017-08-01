import modules.database
import modules.run_search
import modules.postprocessing


def main(args):

    raw_database = args.database
    processed_database = '{}.processed'.format(raw_database)

    spectrum = args.spectrum
    threads = args.threads
    verbose = args.verbose

    spectrum_base = '.'.join(spectrum.split('.')[:-1])

    msfragger_result = spectrum_base + '.pepXML'
    formatted_result = spectrum_base + '.idXML'

    print('######  Preprocessing database  ######')
    modules.database.main(raw_database, processed_database, args.verbose)

    print('######  Executing MSFragger run  ######')
    modules.run_search.run_msfragger(msfragger_jar=args.msfragger_jar,
                                     database_fp=processed_database,
                                     spectrum_fp=spectrum,
                                     out_fp=args.output,
                                     threads=threads,
                                     precursor_mass_tolerance=args.precursor_mass_tolerance,
                                     precursor_mass_units=args.precursor_mass_units,
                                     precursor_true_tolerance=args.precursor_true_tolerance,
                                     precursor_true_units=args.precursor_true_units,
                                     fragment_mass_tolerance=args.fragment_mass_tolerance,
                                     fragment_mass_units=args.fragment_mass_units,
                                     verbose=verbose)

    print('######  Parsing MSFragger output  ######')
    modules.postprocessing.main(msfragger_result, formatted_result)

    print('######  All done!  ######')
