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
 *
 *
 *

  List is coming