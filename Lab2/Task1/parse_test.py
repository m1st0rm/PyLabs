import unittest
import parse_methods as pm


class ParseTest(unittest.TestCase):

    def test_raw_words(self):
        text = 'Something r4nd0m 123 $Dsd'
        raw_words = [
            'Something',
            'r4nd0m',
            '123',
            '$Dsd'
        ]
        self.assertEqual(raw_words, pm.raw_words(text))

    def test_words(self):
        text = 'At lunch, I saw Rep. Charles Rangel.'
        words = [
            'At',
            'lunch',
            'I',
            'saw',
            'Charles',
            'Rangel'
        ]
        self.assertEqual(words, pm.words(text))

    def test_sentences(self):
        text = 'Robert De Niro\'s character Travis Bickle famously asks, "Are you talkin\' to me?".'
        sentences = [
            'Robert De Niro\'s character Travis Bickle famously asks, "Are you talkin\' to me?".'
        ]
        self.assertEqual(sentences, pm.sentences(text))

    def test_sentence_count(self):
        text = 'Hamlet asked whether it was “nobler . . . to suffer the slings and arrows of outrageous fortune or to take arms against a sea of troubles."'
        sentences_count = 1
        self.assertEqual(sentences_count, pm.sentence_count(text))

    def test_non_declarative_sentences(self):
        text = (
            'They spent the day cleaning their living room, kitchen, bedroom, etc. '
            'Adelina wanted to become a doctor after watching the anime Cells at Work!'
        )
        non_declarative_sentences = [
            'Adelina wanted to become a doctor after watching the anime Cells at Work!'
        ]
        self.assertEqual(non_declarative_sentences, pm.non_declarative_sentences(text))

    def test_non_declarative_sentence_count(self):
        text = (
            'Leafy green vegetables such as lettuce, spinach, kale, etc., are an excellent source of nutrition. '
            'Wait a minute . . . If you\'re not watching Charlie, who is?'
        )
        non_declarative_sentences_count = 1
        self.assertEqual(non_declarative_sentences_count, pm.non_declarative_sentence_count(text))

    def test_avg_sentence_length(self):
        text = (
            'Kendal asked what time it was. '
            'Binsa wore her sister\'s gown to the party!'
        )
        avg_sentence_length = 29
        self.assertEqual(avg_sentence_length, pm.avg_sentence_length(text))


    def test_top_n_grams(self):
        text = 'My name is. My name.'
        n = 2
        top_n_grams = [
            ('my name', 2),
            ('name is', 1),
            ('is my', 1)
        ]
        self.assertEqual(top_n_grams, pm.top_n_grams(text, n))
