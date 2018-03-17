import unittest
from search import SearchItem


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SearchItem('test_search_in_main_page'))
    unittest.TextTestRunner(verbosity=2).run(suite)


suite()
