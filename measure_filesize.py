# filename = "./experiments/HumanGenome.fna"
# with open(filename, 'r') as datafile:
#     data = datafile.read()

# data = data[:10]
# print(data)
# # with open(filename, 'w') as datafile:
# #     datafile.write(data)


import os
import pandas as pd

genes = ["AKT1", "APOE", "EGFR", "ESR1", "IL6", "MTHFR", "TGFB1", "TNF", "TP53", "VEGFA"]
genomes = ["ecoli", "scerevisiae"]


def get_path(folder, source):
    return f"./experiments/{folder}/{source}/{source}"


def get_filesizes(path, extension):
    morg = os.path.getsize(f"{path}{extension}")
    mbin = os.path.getsize(f"{path}.bin{extension}")
    mcount = os.path.getsize(f"{path}.count{extension}")
    mbincount = os.path.getsize(f"{path}.bincount{extension}")
    mtargz = os.path.getsize(f"{path}.tar.gz")
    filesize = [morg, mbin, mcount, mbincount, mtargz]

    corg = (1 - morg / morg) * 100
    cbin = (1 - mbin / morg) * 100
    ccount = (1 - mcount / morg) * 100
    cbincount = (1 - mbincount / morg) * 100
    ctargz = (1 - mtargz / morg) * 100
    compression = [corg, cbin, ccount, cbincount, ctargz]

    return filesize + compression


def gather_results(items, location, extension):
    data = pd.DataFrame()
    for item in items:
        path = get_path(location, item)
        results = get_filesizes(path, extension)
        data = data.append(pd.Series(results), ignore_index=True)
    data.index = items
    data.columns = ["org.size", "bin.size", "count.size", "bincount.size", "targz.size",
                    "org.rate", "bin.rate", "count.rate", "bincount.rate", "targz.rate"]
    return data


def write_results(dataframe, path):
    dataframe.to_csv(path)


def main():
    data_genes = gather_results(genes, "genes", ".fasta")
    data_genomes = gather_results(genomes, "genomes", ".fna")
    write_results(data_genes, "./genes_results.csv")
    write_results(data_genomes, "./genomes_results.csv")

if __name__ == "__main__":
    main()
