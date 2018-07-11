from django.test import TestCase
from seq_calcs import sequence_calc


class SeqCalcTestCase(TestCase):
    def setUp(self):
        self.starting_sequence = "ATTGC"

    def test_complement(self):
        complement = sequence_calc.complement(self.starting_sequence)
        self.assertEqual(complement, "TAACG")

    def test_reverse_complement(self):
        reverse_complement = sequence_calc.reverse_complement(self.starting_sequence)
        self.assertEqual(reverse_complement, "GCAAT")

    def test_melting_temp(self):
        melting_temperature = sequence_calc.melting_temp(self.starting_sequence)
        self.assertEqual(melting_temperature, 14.0)

    def test_gc_content(self):
        gc_content = sequence_calc.gc_content(self.starting_sequence)
        self.assertEqual(gc_content, 40.0)
