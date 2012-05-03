from os import path
from unittest import TestCase

from breadability.readable import OriginalDocument


TEST_DIR = path.dirname(__file__)


def load_snippet(filename):
    """Helper to fetch in the content of a test snippet"""
    return open(path.join(TEST_DIR, 'test_snippets', filename)).read()


class TestOriginalDocuemtn(TestCase):
    """Verify we can process html into a document to work off of."""

    def test_readin_min_document(self):
        """Verify we can read in a min html document"""
        doc = OriginalDocument(load_snippet('document_min.html'))
        self.assertTrue(doc.startswith(u'<html>'))
        self.assertEqual(doc.title, 'Min Document Title')

    def test_readin_with_base_url(self):
        """Passing a url should update links to be absolute links"""
        doc = OriginalDocument(load_snippet('document_absolute_url.html'),
            url="http://blog.mitechie.com/test.html")
        self.assertTrue(doc.startswith(u'<html>'))

        # find the links on the page and make sure each one starts with out
        # base url we told it to use.
        links = doc.links
        self.assertEqual(len(links), 3)
        for l in links:
            self.assertEqual(l.startswith('http://blog.mitechie.com/'))

