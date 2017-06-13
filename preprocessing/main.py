import sys
from Bio import SeqIO
import random


def main(args):

    orig_fastas = read_db_fasta(args.input, verbose=args.verbose)
    decoy_fastas = generate_decoy_sequences(orig_fastas, decoy_prefix='r', decoy_type='reverse')
    write_final_fasta(orig_fastas, decoy_fastas, out_fp=args.output)

    if args.verbose:
        print('{} sequences and {} decoys written'.format(len(orig_fastas), len(decoy_fastas)), file=sys.stderr)


def read_db_fasta(db_fp=None, verbose=False):

    """
    Load FASTA files into BioPython records
    Important record fields: seq, id, name, description
    """

    if db_fp is not None:
        in_fh = open(db_fp, 'r')
    else:
        in_fh = sys.stdin
        if verbose:
            print('Reading from STDIN', file=sys.stderr)

    records = list()
    for record in SeqIO.parse(in_fh, 'fasta'):
        records.append(record)

    if db_fp is not None:
        in_fh.close()

    return records


def generate_decoy_sequences(orig_seqs, decoy_prefix='r', decoy_type='reverse'):

    """
    Generate decoy BioSeq entries
    Decoy sequence can be conditionally altered to be reversed or shuffled
    Decoy IDs are prefixed with desired character
    """

    if decoy_type == 'reverse':
        def decoy_func(seq): return seq[::-1]
    elif decoy_type == 'shuffle':
        def decoy_func(seq):
            seq_list = list(seq)
            random.shuffle(seq_list)
            return ''.join(seq_list)
    else:
        raise ValueError('Unknown decoy type: {}'.format(decoy_type))

    decoy_fastas = list()
    for orig_fasta in orig_seqs:
        rev_seq = decoy_func(orig_fasta.seq)
        rev_id = '{}{}'.format(decoy_prefix, orig_fasta.id)

        decoy_entry = SeqIO.SeqRecord(seq=rev_seq,
                                      id=rev_id,
                                      name=orig_fasta.name,
                                      description=orig_fasta.description)
        decoy_fastas.append(decoy_entry)
    return decoy_fastas


def write_final_fasta(orig_fastas, decoy_fastas, out_fp=None):

    """Output the complete set of database FASTA files"""

    all_fastas = orig_fastas + decoy_fastas

    if out_fp is not None:
        out_fh = open(out_fp, 'w')
    else:
        out_fh = sys.stdout

    for rec in all_fastas:
        print('>{}\n{}'.format(rec.id, rec.seq), file=out_fh)

    if out_fp is not None:
        out_fh.close()
