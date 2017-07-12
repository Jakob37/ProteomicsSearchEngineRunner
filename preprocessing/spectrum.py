
import utils.utils as utils


MZML_TO_MGF_COMMAND = '{openms_file_converter} -in {in_fp} -out {out_fp} -in_type {in_type} -out_type {out_type}'


def main(in_fp, out_fp, file_converter_fp, verbose=False):

    command_list = setup_command_list(in_fp, out_fp, MZML_TO_MGF_COMMAND, file_converter_fp)
    utils.run_command(command_list, verbose=verbose)


def setup_command_list(in_fp, out_fp, command_template, file_converter_fp):

    command_string = command_template.format(openms_file_converter=file_converter_fp,
                                             in_fp=in_fp,
                                             out_fp=out_fp,
                                             in_type='mzML',
                                             out_type='mgf')

    return command_string.split(' ')
