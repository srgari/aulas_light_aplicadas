import unittest
import modules.treat_tables as tt

import pandas as pd 


class Test_join_tables(unittest.TestCase):
    df = tt.join_tables('dados_clientes')
    first_table = pd.read_csv('input/dados_clientes_jan.csv')
    def test_1_function_join_tables(self):        
        assert len(self.df) > 0, 'Dataframe generated is empty!'
        assert len(self.df) > len(self.first_table), 'Dataframe generated is too small!'


    def test_2_number_of_males_and_females(self):
        assert (
            len(self.df.query('sexo == "M"')) 
            + len(self.df.query('sexo == "F"')) 
            == len(self.df)
        ), 'total men and women is less than total people!'



if __name__ == '__main__':
    unittest.main()





