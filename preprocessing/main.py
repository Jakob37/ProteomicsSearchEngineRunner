import preprocessing.database
import preprocessing.spectrum


OPENMS_FILE_CONVERTER = 'binaries/FileConverter'


def preprocess_database(args):

    preprocessing.database.main(args)


def preprocess_spectrum(args):

    preprocessing.spectrum.main(args.input, args.output, OPENMS_FILE_CONVERTER, verbose=args.verbose)


