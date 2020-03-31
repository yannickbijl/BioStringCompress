# BioStringCompress (BSC)
BioStringCompress is a commandline tool for efficient compression of biological sequences (DNA/for long term storage.

## Usage

The tool can be used using the following command when in the main folder of this project.

`python3 BioStringCompress.py [-h] -i INPUT -o OUTPUT [-d {True,False}] [-m {bin,count,bincount}]`

Tests (using pytest) can be run from the main folder of this project with the command:

`python3 -m pytest`

## Motivation
Biological sequences provide a wealth of information, and each year there are improvements in the field are made.
Increasing the length of the reads is one of the major improvements made.
However, while the cost of measuring and analyzing sequencing data becomes increasingly cheaper, storing such data does not become cheaper at the same rate.

Thus efficient data storage becomes necessary. Therefore, we have developed three straightforward methods. With these methods we have decided to take more than the 4 nucleotides into account. This includes gaps and other standard symbols ([link](https://www.bioinformatics.org/sms/iupac.html)) for DNA/RNA sequences, totaling 16 symbols.

## Methods
### bin
Transform each base (8 bits) into 4 bits. This theoretically decreases the data size by half. In practice, computer systems can only store bytes (8 bits). Thus in the case of an uneven number of bases, we need to add an additional 4 bits. We have chosen do add a gap in that case. Therefore the worstcase compression rate is half the data size plus 4 bits.

### count
Biological sequences are not entirely random, with many repeating sections. The method compresses the data by simplifying the sequence. If a base is repeated after each other, the data can be represented as the number of occurrence and the base itself. Thus `AAAAATTGCCC` becomes `5A2T1G3C`.

### bincount
This last method takes a mixed approach of the previous two methods. It compresses the sequence in the same manner as `count`, with the number being a maximum of 16, as this can still be stored into 4 bits. The number and base are both converted into bits. As each base is accompanied with a number, there is no need to add additional bits.

# To Be Removed Later
## TODO:
  - [x] Update README
  - [x] Write test scripts for BSC
  - [x] Experiments for effectiveness of compression methods
    - [x] Gene: [TNF](https://www.ncbi.nlm.nih.gov/search/all/?term=TNF) (RefSeqGene)
    - [-] Sequence Alignment (Consensus Sequence): Generate self.
    - [-] Genome: [human genome GRCh38.p13](https://www.ncbi.nlm.nih.gov/search/all/?term=human%20genome) (Select `Genomic FASTA` for File Type)
  - [x] Plot results of experiments
    - [x] measure compression factor (filesize)
    - [-] measure decompression accuracy (reconstruction)
  - [] Write report/article

## Papers
 * [Biological Sequence Compression Algorithms](https://www.jsbi.org/pdfs/journal1/GIW00/GIW00F05.pdf)
 * [SeqCompress: An algorithm for biological sequence compression](https://www.sciencedirect.com/science/article/pii/S0888754314001499)
 * [A Survey on Data Compression Methods for Biological Sequences](https://www.mdpi.com/2078-2489/7/4/56/htm)
 * [MFCompress: a compression tool for FASTA and multi-FASTA data](https://academic.oup.com/bioinformatics/article/30/1/117/236841)
