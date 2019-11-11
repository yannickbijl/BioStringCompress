# SeqCompress
 Efficient compression of biological sequences for long term storage.

## 3 (de)compression methods
Normally all bases are stored using 8-bit characters.
There are 16 options for nucleotide encoding, see [here](https://www.bioinformatics.org/sms/iupac.html). Thus it can be stored more efficiently as

 1. 4-bit encoding for a nucleotide as 4 bits gives 16 options. This should compress any file by circa 50%.

 However, biological sequences are not randomly ordered. Having many regions with the same symbol. Ths we use another approach

 2. Where each series of same symbols is collapsed. With this method we do use 8-bit character representation. Thus AAAAGTTT -> 4AG3T or A4G3T

 This approach can also be turned into a version using bits, this does require an additional bit for identifying numbers and a set number of bits for representing numbers. This last part should be as low number as bits as is acceptable.

 3. AAAAGTTT -> 1 0000 11 0 1000 1 0100 01 = True A 4 False G True T 3

## Experiments
 Measure compression efficiency on several datasets of different sizes. So as example:

 * a gene
 * a chromosome
 * a genome


## Papers
 * [Biological Sequence Compression Algorithms](https://www.jsbi.org/pdfs/journal1/GIW00/GIW00F05.pdf)
 * [SeqCompress: An algorithm for biological sequence compression](https://www.sciencedirect.com/science/article/pii/S0888754314001499)
 * [A Survey on Data Compression Methods for Biological Sequences](https://www.mdpi.com/2078-2489/7/4/56/htm)
 * [MFCompress: a compression tool for FASTA and multi-FASTA data](https://academic.oup.com/bioinformatics/article/30/1/117/236841)

 ## TODO
  * Figure out how to save strings of 1 and 0 to actual bytes.
  * Write sequence parser.
  * Write byte parser.
  * Figure out how to determine file size accurately.
  * Think of other name than SeqCompress.