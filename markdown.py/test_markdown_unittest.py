'''
Test markdown.py with unittest
To run tests:
    python test_markdown_unittest.py
'''

import unittest
from markdown_adapter import run_markdown


class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual(
            run_markdown('this line has no special handling'),
            '<p>this line has no special handling</p>')

    def test_em(self):
        '''
        Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual(
            run_markdown('*this should be wrapped in em tags*'),
            '<p><em>this should be wrapped in em tags</em></p>')

    def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual(
            run_markdown('**this should be wrapped in strong tags**'),
            '<p><strong>this should be wrapped in strong tags</strong></p>')

    def test_header(self):
        self.assertEqual(run_markdown('###Header 3'), '<h3>Header 3</h3>')

    def test_header2(self):
        self.assertEqual(run_markdown(
            '## This is an H2 in a blockquote'), '<h2> This is an H2 in a blockquote</h2>')

    def test_header3(self):
        self.assertEqual(run_markdown(
            '# This is an H2 in a blockquote'), '<h1> This is an H2 in a blockquote</h1>')

    def test_block(self):
        self.assertEqual(run_markdown(
            '> This is a blockquote.\n> \n> This is the second paragraph in the blockquote.\n\n'), '<blockquote>\n<p>This is a blockquote.</p>\n\n<p>This is the second paragraph in the blockquote.</p>\n</blockquote>')

if __name__ == '__main__':
    unittest.main()
