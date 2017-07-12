import preprocessing.database
import preprocessing.spectrum


def preprocess_database(args):

    preprocessing.database.main(args.input, args.output, args.verbose)


def preprocess_spectrum(args):

    preprocessing.spectrum.main(args.input, args.output, verbose=args.verbose)
