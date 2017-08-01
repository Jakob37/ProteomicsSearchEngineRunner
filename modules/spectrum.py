from modules import utils as utils

MZML_TO_MGF_COMMAND = '{openms_file_converter} -in {in_fp} -out {out_fp} -in_type {in_type} -out_type {out_type}'
OPENMS_FILE_CONVERTER = '{openms_bin}/FileConverter'


def preprocess_spectrum(args):

    file_converter_fp = OPENMS_FILE_CONVERTER.format(openms_bin=args.openms_bin)

    command_string = MZML_TO_MGF_COMMAND.format(
        openms_file_converter=file_converter_fp,
        in_fp=args.input,
        out_fp=args.output,
        in_type='mzML',
        out_type='mgf'
    )

    command_list = command_string.split(' ')
    utils.run_command(command_list, verbose=args.verbose)
