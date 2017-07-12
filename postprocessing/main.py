import utils.utils as utils


PEPXML_TO_IDXML_COMMAND = '{openms_id_converter} -in {in_fp} -out {out_fp} -out_type {out_type}'


def main(in_fp, out_fp, file_converter_fp, verbose=False):

    command_list = setup_command_list(in_fp, out_fp, PEPXML_TO_IDXML_COMMAND, file_converter_fp)
    utils.run_command(command_list, verbose=verbose)


def setup_command_list(in_fp, out_fp, command_template, id_converter_fp):

    command_string = command_template.format(
        openms_id_converter=id_converter_fp,
        in_fp=in_fp,
        out_fp=out_fp,
        out_type='idXML'
    )

    return command_string.split(' ')
