import argparse

import libs


parser = argparse.ArgumentParser()
parser.add_argument('mode', type=boolean, help="Setting for compression (True) or decompression (False).", default=True)
parser.add_argument('seq', type=string, help="File with sequence.")
args = parser.parse_args()

sequence = SeqData(args.seq)
if args.mode:
    Compress.compress_4bit()
else:
    Decompress.decompress_4bit()