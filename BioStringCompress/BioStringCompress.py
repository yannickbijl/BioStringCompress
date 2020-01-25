import argparse

import lib_data

import lib_compress
import lib_decompress

import lib_exceptions

# load logger and set as global variable.
import lib_logger
logger = lib_logger.startLogger()


def compressData(data, method) -> list:
    if method == 'bin':
        return lib_compress.binCompress(data)
    elif method == 'count':
        return lib_compress.countCompress(data)
    elif method == 'bincount':
        return lib_compress.binCountCompress(data)
    else:
        logger.debug(f'The method "{method}" has not been implemented for compression.')
        raise lib_exceptions.FeatureNotImplemented(f'The method "{method}" has not been implemented for compression.')


def decompressData(data, method:str) -> list:
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
    parser.add_argument('-i', '--input', dest='input', type=str, required=True,
                        help="")
    parser.add_argument('-o', '--output', dest='output', type=str, required=True
                        , help="")
    parser.add_argument('-d', '--direction', dest='direction', type=str,
                        required=False, default='True', choices=['True', 'False'],
                        help="")
    parser.add_argument('-m', '--method', dest='method', type=str, required=False
                        , default='bincount', choices=['bin', 'count', 'bincount'], help="")
    parser.add_argument('-t', '--type', dest='type', type=str, required=False,
                        default='DNA', choices=['DNA', 'RNA'], help="")
    args = parser.parse_args()
    logger.info("Arguments parsed.")

    if args.direction == 'True': # Compression
        logger.info("Data will be compressed.")

        logger.debug(f"Load data in file '{args.input}'.")
        inputData = lib_data.readNormal(args.input)
        logger.info("Data loaded.")

        if args.type == 'RNA':
            inputData = lib_data.translateRNAToDNA(inputData)

        logger.debug(f"Compress data using method '{args.method}'.")
        outputData = compressData(inputData, args.method)
        logger.info("Data is compressed.")

        logger.debug(f"Write compressed data to file '{args.output}'.")
        if args.method in ['bin', 'bincount']:
            lib_data.writeBinary(args.output, outputData)
        else:
            lib_data.writeNormal(args.output, outputData)
        logger.info("Compressed data is written.")

    else: # Decompression
        logger.info("Data will be decompressed.")

        logger.debug(f"Load data in file '{args.input}'.")
        if args.method in ['bin', 'bincount']:
            inputData = lib_data.readBinary(args.input)
        else:
            inputData = lib_data.readNormal(args.input)
        logger.info("Data loaded.")

        logger.debug(f"Decompress data using method '{args.method}'.")
        outputData = decompressData(inputData, args.method)
        logger.info("Data is decompressed.")

        if args.type == 'RNA':
            outputData = lib_data.translateDNAToRNA(outputData)

        logger.debug(f"Write decompressed data to file '{args.output}'.")
        lib_data.writeNormal(args.output, outputData)
        logger.info("Decompressed data is written.")

    logger.info("Successfully excecuted program 'BioStringCompress'.")

if __name__ == "__main__":
    main()
