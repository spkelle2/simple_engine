import unittest
from simple_engine import input_schema, solve


class TestDiet(unittest.TestCase):

    def test_good_solve(self):
        input_dat = input_schema.TicDat()
        input_dat.parameters = {'run_solve': {'Value': 'yes'}}
        sln_dat = solve(input_dat)
        self.assertEqual(sln_dat.parameters['run_solve']['Value'],
                         input_dat.parameters['run_solve']['Value'])


if __name__ == '__main__':
    unittest.main()
