import unittest

# 'word'
MEDIA_1_WORD = '/media_files/media_1_word.wav'
# 'word word word'
MEDIA_SENTENCE = '/media_files/media_sentence.wav'


class MyTestCase1(unittest.TestCase):
    def test_1_word(self):
        print('test_1_simple_sentence')
        expected_text = 'word'
        actual_text = v2t(MEDIA_1_WORD)
        self.assertEqual(actual_text, expected_text)

    def test_1_simple_sentence(self):
        print('test_1_word')
        expected_text = 'word word word'
        actual_text = v2t(MEDIA_SENTENCE)
        self.assertEqual(actual_text, expected_text)


if __name__ == '__main__':
    unittest.main()
