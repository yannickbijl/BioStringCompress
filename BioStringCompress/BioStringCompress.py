import argparse

import lib_data

import lib_compress
import lib_decompress

# load logger and set as global variable.
import lib_logger
logger = lib_logger.start_logger()

def main():
    logger.info("Start program 'BioStringCompress'")

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', type=str, required=True
                        , help="")
    parser.add_argument('-o', '--output', dest='output', type=str, required=True
                        , help="")
    parser.add_argument('-d', '--direction', dest='direction', type=bool,
                        required=False, default=True)
    parser.add_argument('-m', '--method', dest='method', type=str, required=False
                        , default='a', choices=['a', 'b', 'c'], help="")
    args = parser.parse_args()

    # Read data
    if args.direction:
        pass
        # compress data
    else:
        pass
        # decompress data
    # Write data

if __name__ == "__main__":
    main()