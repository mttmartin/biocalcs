
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import MeltingTemp as mt
from Bio.SeqUtils import GC

def reverse_complement(input_str):
    seq = Seq(input_str, IUPAC.unambiguous_dna)
    return seq.reverse_complement()

def complement(input_str):
    seq = Seq(input_str, IUPAC.unambiguous_dna)
    return seq.complement()

def melting_temp(input_str):
    seq = Seq(input_str, IUPAC.unambiguous_dna)
    return mt.Tm_Wallace(seq)

def gc_content(input_str):
    seq = Seq(input_str, IUPAC.unambiguous_dna)
    return GC(seq)

