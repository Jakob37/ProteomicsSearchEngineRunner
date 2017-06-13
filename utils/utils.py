import time
import subprocess


def run_command(command_list, verbose=False):

    start_time = time.time()
    if verbose:
        print(' '.join(command_list))

    p = subprocess.Popen(command_list)
    p.wait()

    elapsed_time = time.time() - start_time
    if verbose:
        print('Command finished after {} seconds'.format(elapsed_time))
