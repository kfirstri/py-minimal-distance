import unittest
import minimal

class TestMinimalFunctions(unittest.TestCase):

    def test_get_sentences_only_period(self):
        text = 'John Doe aaa bbb ccc ddd love music. John Doe aaa not love music.'
        first = 'John Doe aaa bbb ccc ddd love music.'
        second = 'John Doe aaa not love music.'

        res = minimal.get_sentences(text)

        self.assertEqual(len(res), 2)
        self.assertEqual(res[0], first)
        self.assertEqual(res[1], second)
        
    def test_get_sentences_with_ex_mark(self):
        text = 'John Doe aaa bbb ccc ddd love music!!! John Doe aaa not love music.'
        first = 'John Doe aaa bbb ccc ddd love music!!!'
        second = 'John Doe aaa not love music.'

        res = minimal.get_sentences(text)

        self.assertEqual(len(res), 2)
        self.assertEqual(res[0], first)
        self.assertEqual(res[1], second)

if __name__ == '__main__':
    unittest.main()