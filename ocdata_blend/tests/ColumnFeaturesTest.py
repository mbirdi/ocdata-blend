# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

import unittest
from pandas import DataFrame
from ColumnFeatures_2 import ColFeatures


class ColumnfeaturesTest(unittest.TestCase):
    
    def test_data_not_zero(self):
    	list_of_list = [('id', 'procurring_entity_id', 'tender_type' , 'tender_registration_number'), ('Brian', 'unladen swallow', 'dead parrot' , '2') ]
    	data = pd.DataFrame(list_of_list)
    	cF = ColFeatures(data)
        self.assertNotEqual(cF.get_col_names(), 0.0)
        
    def test_returns_col_names(self):
    	data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002],'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    	frame = pd.DataFrame(data)
        
        ##  Here the class is instantiated
        cF = ColFeatures(frame)
        
        actual = cF.get_col_names()
        
        ##print actual
        
        ##self.assertNotEqual(cF.get_col_names(), 0.0)
        expected = ['pop', 'state', 'year']
        
        self.assertListEqual(actual, expected, msg='Lists did not match')
