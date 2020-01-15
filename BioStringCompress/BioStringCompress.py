import argparse

import lib_data

import lib_compress
import lib_decompress

import lib_exceptions

# load logger and set as global variable.
import lib_logger
logger = lib_logger.start_logger()


def compress_data(data, method):
    logger.info(f'Data is compressed using the method "{method}".')
    if method == 'bin':
        return lib_compress.binCompress(data)
    elif method == 'count':
        return lib_compress.countCompress(data)
    elif method == 'bincount':
        return lib_compress.binCountCompress(data)
    else:
        logger.debug(f'The method "{method}" has not been implemented for compression.')
        raise lib_exceptions.FeatureNotImplemented(f'The method "{method}" has not been implemented for compression.')


def decompress_data(data, method:str):
    logger.info(f'Data is decompressed using the method "{method}".')
    if method == 'bin':
        return lib_decompress.binDecompress(data)
    elif method == 'count':
        return lib_decompress.countDecompress(data)
    elif method == 'bincount':
        return lib_decompress.binCountDecompress(data)
    else:
        logger.debug(f'The method "{method}" has not been implemented for decompression.')
        raise lib_exceptions.FeatureNotImplemented(f'The method "{method}" has not been implemented for compression.')


def main():
    logger.info("Start program 'BioStringCompress'.")

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', type=str, required=True
                        , help="")
    parser.add_argument('-o', '--output', dest='output', type=str, required=True
                        , help="")
    parser.add_argument('-d', '--direction', dest='direction', type=bool,
                        required=False, default=True)
    parser.add_argument('-m', '--method', dest='method', type=str, required=False
                        , default='bincount', choices=['bin', 'count', 'bincount'], help="")
    args = parser.parse_args()

    if args.direction: # Compression
        in_data = lib_data.read_normal(args.input)
        out_data = compress_data(in_data, args.method)
        if args.method in ['bin', 'bincount']:
            lib_data.write_binary(out_data, args.output)
        else:
            lib_data.write_normal(out_data, args.output)
    else: # Decompression
        if args.method in ['bin', 'bincount']:
            in_data = lib_data.read_binary(args.input)
        else:
            in_data = lib_data.read_normal(args.input)
        out_data = decompress_data(in_data, args.method)
        lib_data.write_normal(out_data, args.output)

    logger.info("Successfully excecuted program 'BioStringCompress'.")

if __name__ == "__main__":
    main()
