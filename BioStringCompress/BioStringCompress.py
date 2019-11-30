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
    if method == 'a':
        return lib_compress.a(data)
    elif method == 'b':
        return lib_compress.b(data)
    elif method == 'c':
        return lib_compress.c(data)
    else:
        logger.debug(f'The method "{method}" has not been implemented for compression.')
        raise lib_exceptions.FeatureNotImplemented(f'The method "{method}" has not been implemented for compression.')


def decompress_data(data, method):
    logger.info(f'Data is decompressed using the method "{method}".')
    if method == 'a':
        return lib_decompress.a(data)
    elif method == 'b':
        return lib_decompress.b(data)
    elif method == 'c':
        return lib_decompress.c(data)
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
                        , default='a', choices=['a', 'b', 'c'], help="")
    args = parser.parse_args()

    if args.direction:
        in_data = lib_data.read_normal(args.input)
        out_data = compress_data(in_data, args.method)
        lib_data.write_binary(out_data, args.output)
    else:
        in_data = lib_data.read_binary(args.input)
        out_data = compress_data(in_data, args.method)
        lib_data.write_binary(out_data, args.output)

    logger.info("Successfully excecuted program 'BioStringCompress'.")

if __name__ == "__main__":
    main()
