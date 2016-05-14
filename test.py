import unittest

import q08

class Testq08(unittest.TestCase):

    def test_case_where_it_matters(self):
        problem = ('1',
                   '2',
                   'Yeehaw',
                   'NSM',
                   '5',
                   'NSM',
                   'Yeehaw',
                   'NSM',
                   'Yeehaw',
                   'NSM')
        problem = problem.__iter__()
        solution = ['Case #1: 4\n']
        self.assertEqual(q08.solve(problem), solution)


if __name__ == '__main__':
    unittest.main()
