import unittest

# 'before command delete after'
MEDIA_DELETE = '/media_files/media_delete.wav'

# 'command delete'
MEDIA_DELETE_NOTHING_BEFORE = '/media_files/media_delete_nothing_before.wav'


class MyTestCase1(unittest.TestCase):
    def test_command_delete(self):
        print('test_command_delete')
        expected_text = 'before after'
        actual_text = v2t(MEDIA_DELETE)
        self.assertEqual(actual_text, expected_text)

    def test_command_delete_nothing_before(self):
        print('test_command_delete_nothing_before')
        expected_text = ''
        actual_text = v2t(MEDIA_DELETE_NOTHING_BEFORE)
        self.assertEqual(actual_text, expected_text)


if __name__ == '__main__':
    unittest.main()
