from modules import utils as utils

PEPXML_TO_IDXML_COMMAND = '{openms_id_converter} -in {in_fp} -out {out_fp} -out_type {out_type}'
OPENMS_ID_CONVERTER = '{openms_bin}/IDFileConverter'


def main(in_fp, out_fp, openms_bin, verbose=False):

    openms_command = OPENMS_ID_CONVERTER.format(openms_bin=openms_bin)

    command_string = PEPXML_TO_IDXML_COMMAND.format(
        openms_id_converter=openms_command,
        in_fp=in_fp,
        out_fp=out_fp,
        out_type='idXML'
    )

    command_list = command_string.split(' ')
    utils.run_command(command_list, verbose=verbose)
